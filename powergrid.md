# Network data of power grids

(updated 10 May, 2016)
**Heetae Kim** 
- E-mail: [kimheetae at Gmail](kimheetae@gmail.com)
- Department of Energy Science, Sungkyunkwan University



We introduce the network data of power grids available in public. Only the web-based data sources are considered with the direct url links. The data are provided in various forms as each provider prepared. Some data need validation before use. For example, edge straightening, node reduction, missing nodes or edges check are frequently required for handling power-grid networks. Next update would provide the unifided file format of the data sources.
Please, kindly inform the author about any missing network data from this list.


## Summary
|Model/project|Region|Nodes|Edges|Type|Repository|
|---|---|---|---|---|---|
|SciGrid|Germany|495|825|F|[Link](http://www.scigrid.de/pages/downloads.html)|
|GridKit|North America|16174|22459|F|[Link](http://dx.doi.org/10.5281/zenodo.47317)|
|GridKit|Europe|13871|18804|F|[Link](http://dx.doi.org/10.5281/zenodo.47317)|
|Bialek model|Europe|1497|2322|F|[Link](http://www.powerworld.com/knowledge-base/updated-and-validated-power-flow-model-of-the-main-continental-european-transmission-network)|
|Geo-tagged Bialek|Europe|1494|2156|F|[Link](http://dx.doi.org/10.5281/zenodo.35177)|
|ELMOD-DE|Germany|438|697|F|[Link](http://www.diw.de/de/diw_01.c.528493.de/forschung_beratung/nachhaltigkeit/umwelt/verkehr/energie/modelle/elmod.html#ELMOD-DE)|
|National grid|the UK|1060|1192|FM|[Link](http://www2.nationalgrid.com/UK/Industry-information/Future-of-Energy/Electricity-ten-year-statement/ETYS-Archive/)|
|ENTSO-E|Europe|>7,000|>8,000|FMI|[Interactive map](https://www.entsoe.eu/map/Pages/default.aspx)/[Data request](https://www.entsoe.eu/stum)|
|Energinet.dk|Denmark|341|393|FM|[Data, grid map](http://www.energinet.dk/DA/El/Udvikling-af-elsystemet/Netplanlaegning/Sider/Formular-Til-Download-Af-Netdata.aspx)|
|RTE|France|829|236|F|[Link](https://clients.rte-france.com/lang/an/visiteurs/vie/indispos_caracteristiques_statiques.jsp)|
|Elia|Belgium|57|80|FM|[Data](http://www.elia.be/en/grid-data/Grid-Technical-Data)/[Grid map](http://www.elia.be/en/about-elia/publications/maps)
|CEPS|The Czech Repubic|46|63|M|[Grid map](https://www.ceps.cz/ENG/Cinnosti/Technicka-infrastruktura/Pages/Udaje-o-PS.aspx)|
|Australia|Australia|909|2090|FMI|[Nodes](http://www.data.gov.au/dataset/national-electricity-transmission-substations), [Edges](http://www.data.gov.au/dataset/national-electricity-transmission-lines-database)|
|Watts and Strogatz|Western US|4941|6594|F|[Link 1](http://nexus.igraph.org/api/dataset_info?id=15&format=html),[Link 2](https://networkdata.ics.uci.edu/data.php?id=107),[Link 3](https://toreopsahl.com/datasets/#uspowergrid)|
|Kim et al.|Chile|420|573|F|[Link](http://iopscience.iop.org/article/10.1088/1367-2630/17/11/113005/meta)|
Type: F = data file, M = grid map, I = interactive information

## By region
- Germany: [SciGRID project](http://www.scigrid.de/pages/downloads.html)

- Denmark: [energinet.dk](http://www.energinet.dk/DA/El/Udvikling-af-elsystemet/Netplanlaegning/Sider/Formular-Til-Download-Af-Netdata.aspx)

- France: [Static grid model](https://clients.rte-france.com/lang/an/visiteurs/vie/indispos_caracteristiques_statiques.jsp)

- Belgium: [Activity data](http://www.elia.be/en/grid-data/data-download) / [grid map 1](http://www.elia.be/en/about-elia/publications/maps) / [grid map 2](http://www.elia.be/~/media/images/Elia/Grid%20data/map_Grid-Technical-Data_en.jpg?la=en)

- Czech Republic: [Grid map](https://www.ceps.cz/ENG/Cinnosti/Technicka-infrastruktura/Pages/Udaje-o-PS.aspx)

- Australia:  [Transmission substations](http://www.data.gov.au/dataset/national-electricity-transmission-substations) / [Transmission lines](http://www.data.gov.au/dataset/national-electricity-transmission-lines-database)

- Europe - Bialek model: [Original version](http://www.powerworld.com/knowledge-base/updated-and-validated-power-flow-model-of-the-main-continental-european-transmission-network) / [Geo-tagged Bialek](http://dx.doi.org/10.5281/zenodo.35177)

- Europe - ENTSO-E: [Interactive map](https://www.entsoe.eu/map/Pages/default.aspx) / [Statistics](https://www.entsoe.eu/news-events/former-associations/ucte/graphical-statistics/Pages/default.aspx) / [Data portal](https://www.entsoe.eu/data/data-portal/Pages/default.aspx)

- Europe - Open Power System Data: [Homepage](http://open-power-system-data.org)

- Western US: [NEXUS repository](http://nexus.igraph.org/api/dataset_info?id=15&format=html) / [The UCI network data repository](https://networkdata.ics.uci.edu/data.php?id=107) / [Tore Opsahl site](https://toreopsahl.com/datasets/)

- Chile: [Download](https://sites.google.com/site/heetae/Home/chilean-power-grid/chilean_power_grid.xls?attredirects=0&d=1)

- South Africa: [shape file](http://infrastructureafrica.org/documents/tools/list/arcgis-shape-files)


## Power-grid toolkits

- SciGRID: [Homepage](http://www.scigrid.de)
- Gridkit: [Homepage](https://github.com/bdw/GridKit)
- osmTGmod: [Homepage](https://github.com/maltesc/osmTGmod)

## Interactive information
- US: [Energy-graph](http://www.energy-graph.com/index.html)
- The world: [Enipedia](http://enipedia.tudelft.nl/maps/PowerPlants.html)
- Europe: [ENTSO-E](https://www.entsoe.eu/map/Pages/default.aspx)

## Graphical data

- Denmark: [energinet.dk](http://www.energinet.dk/DA/El/Udvikling-af-elsystemet/Netplanlaegning/Sider/Formular-Til-Download-Af-Netdata.aspx)
- Belgium: [elia.be](http://www.elia.be/en/grid-data/Grid-Technical-Data)([direct download](http://www.elia.be/~/media/files/Elia/publications-2/maps/map-of-the-high-voltage-grid_2016.pdf))
- The world: [GENI](http://www.geni.org/globalenergy/library/national_energy_grid/index.shtml) (not professional source)
- Peru: [Link](http://www.minem.gob.pe/_publicacion.php?idSector=6&idPublicacion=395)

## Free softwares for power system analysis
- [PyPower](https://github.com/rwl/PYPOWER) in Python
- [PyPSA](https://github.com/FRESNA/PyPSA) in Python for Power System Analysis
- [PowerGAMA](https://bitbucket.org/harald_g_svendsen/powergama/wiki/Home) in Python
- [MATPOWER](http://www.pserc.cornell.edu/matpower/) in Matlab or Octave
- [OpenDSS](http://sourceforge.net/projects/electricdss/) in Pascal
- [PSAT](http://faraday1.ucd.ie/psat.html) in Matlab or Octave

## Other network data repositories
- https://networkdata.ics.uci.edu/index.php
- http://nexus.igraph.org
- https://toreopsahl.com/datasets
