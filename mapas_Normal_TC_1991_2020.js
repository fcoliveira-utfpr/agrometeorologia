// ==========================================================
// 1) Definição de Regiões
// ==========================================================
var brasil = ee.FeatureCollection('FAO/GAUL/2015/level0')
  .filter(ee.Filter.eq('ADM0_NAME', 'Brazil'));
  
var estados = ee.FeatureCollection('FAO/GAUL/2015/level1')
  .filter(ee.Filter.eq('ADM0_NAME', 'Brazil'));

// ==========================================================
// 2) Carregamento e Filtro (1991-2020)
// ==========================================================
var dataset = ee.ImageCollection('IDAHO_EPSCOR/TERRACLIMATE')
  .filterBounds(brasil)
  .filterDate('1991-01-01', '2020-12-31');

// ==========================================================
// 3) Processamento: Médias vs Somas Anuais
// ==========================================================
var anos = ee.List.sequence(1991, 2020);

// Variáveis de ACÚMULO (Soma anual média de 30 anos)
var normalAcumulo = ee.ImageCollection.fromImages(
  anos.map(function(ano) {
    return dataset.filter(ee.Filter.calendarRange(ano, ano, 'year'))
      .select(['pr', 'pet', 'def', 'srad', 'soil'])
      .sum()
      .set('year', ano);
  })
).mean();

// Variáveis de ESTADO (Média aritmética de todos os meses do período)
var normalEstado = dataset.select(['tmmx', 'tmmn']).mean();

// ==========================================================
// 4) Consolidação e Fatores de Escala (0.1)
// ==========================================================
var climatologiaAnual = ee.Image.cat([
  normalAcumulo.select('pr'), // pr não multiplica
  normalAcumulo.select('pet').multiply(0.1).rename('pet'),
  normalAcumulo.select('def').multiply(0.1).rename('def'),
  normalAcumulo.select('srad').multiply(0.1).rename('srad'),
  normalEstado.select('tmmx').multiply(0.1).rename('tmmx'),
  normalEstado.select('tmmn').multiply(0.1).rename('tmmn'),
  normalAcumulo.select('soil').multiply(0.1).rename('soil')
]).clip(brasil);

// ==========================================================
// 5) Visualização de TODAS as Variáveis no Mapa
// ==========================================================
Map.centerObject(brasil, 4);

// Temperaturas (Médias)
Map.addLayer(climatologiaAnual.select('tmmx'), {min: 15, max: 35, palette: ['blue', 'green', 'yellow', 'red']}, '1. Temp Máxima Média (°C)');
Map.addLayer(climatologiaAnual.select('tmmn'), {min: 5, max: 25, palette: ['blue', 'green', 'yellow', 'red']}, '2. Temp Mínima Média (°C)');

// Chuva e Água (Totais Anuais e Médias)
Map.addLayer(climatologiaAnual.select('pr'), {min: 500, max: 3000, palette: ['white', '#74add1', '#313695']}, '3. Precipitação Total Anual (mm)');
Map.addLayer(climatologiaAnual.select('pet'), {min: 1000, max: 2500, palette: ['#ffffb2', '#fd8d3c', '#bd0026']}, '4. PET Total Anual (mm)');
Map.addLayer(climatologiaAnual.select('soil'), {min: 200, max: 3000, palette: ['#ece7f2', '#a6bddb', '#2b8cbe']}, '5. Umidade Solo Média (mm)');

// Energia e Déficit (Totais Anuais)
Map.addLayer(climatologiaAnual.select('def'), {min: 0, max: 1000, palette: ['#e5f5f9', '#99d8c9', '#2ca25f']}, '6. Déficit Hídrico Anual (mm)');
Map.addLayer(climatologiaAnual.select('srad'), {min: 2000, max: 3500, palette: ['#fff7bc', '#fec44f', '#d95f0e']}, '7. Radiação Solar Anual (W/m2)');

// Limites
Map.addLayer(estados.style({color: 'black', fillColor: '00000000', width: 0.5}), {}, 'Estados');

// ==========================================================
// 6) Exportação (Todas as 7 bandas)
// ==========================================================
Export.image.toDrive({
  image: climatologiaAnual,
  description: 'Normal_Climatica_ANUAL_Completa_BR_91_20',
  folder: 'GEE_Exports',
  scale: 4638, 
  region: brasil.geometry().bounds(),
  fileFormat: 'GeoTIFF'
});

print('Processamento concluído. Verifique as camadas no painel Layer.');
