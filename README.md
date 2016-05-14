https://pcjericks.github.io/py-gdalogr-cookbook/index.html #jsta

# Welcome to the NEON Working with Vector Data in Python Tutorial Series Git Repo!
This repo is the building space for lessons on working with Vector Data in Python.
Once the lessons are developed and ready for publication, the lessons are moved
to and published in the NEON Data Skills Git Repo and live at
[www.neondataskills.org](http://www.neondataskills.org).

# NEON Science & Education
NEON Data Skills provides tutorials and resources for working with scientific
data. NEON
[(National Ecological Observatory Network](http://www.neonscience.org])
is an ecological observatory, solely funded by the National Science Foundation
that will collect and provide open data for 30 years.

[www.neondataskills.org](http://www.neondataskills.org)

Education is a key component of the NEON mission. As such this site serves to
facilitate use of data in both science and education.

---

### Work with Spatio-temporal Data in Python -- Data Theme: Phenology
The original R materials were developed during a lesson building hack-a-thon
jointly organized by Leah Wasser (NEON), Tracy Teal (Data Carpentry), Mike
Smorul (National Socio-Environmental Synthesis Center (SESYNC) and Jason William
(iPlant Collaborative).

Hack-a-thon participants included Mike Alonzo, Sean Barberie, Ben Best,
Zack Bryn, Jonah Duckles, Marisa Guarinello, Jeff Hollister, Megan A. Jones,
Matthew Kwit, Kristina Riemer, Dave Roberts, Keely Roth, Mike Smorul,
Courtney Soderberg, Joseph Stachelek, Kaitlin Stack Whitney, Tracy Teal,
Leah A. Wasser, Jason Williams, and Meg Williams.

The results of this collaboration are four tutorial
series hosted on the NEON Data Skills portal (neondataskills.org) and also
taught as Data Carpentry workshops (www.datacarpentry.org).  

* Introduction to Working With Spatio-Temporal Data and Data Management
* Introduction to Working With Raster Data in R
* Working With Raster Time Series Data in R
* Introduction to Working With Time Series Data in Text Formats in R

## Python environment
Install Anaconda (or Miniconda) and setup a Python environment using the following console commands:

```
$ conda create --name fiona python=3 fiona=1.1.6
$ source activate fiona
$ conda install fiona=1.1.6
$ conda install -c ioos geopandas=0.2.0.dev0
$ conda install rasterio=0.25
$ conda install -c ioos cartopy=0.14.2
```

## Contributors
Joseph Stachelek converted the original R material to Python.

## Teaching Data Subsets
Data used in these lessons, can be found on the
<a href="https://figshare.com/authors/NEON_Data_Skills_Teaching_Data_Subsets/834136" target="_blank"> NEON Data Skills Teaching Data Subsets figshare page </a>.

### Spatio-temporal Series Teaching Data Subsets
This data was curated into a teaching data subset by Leah A. Wasser. Original
sources of the data include
<a href="http://www.neoninc.org/data-resources/get-data/airborne-data" target="_blank"> NEON Airborne Data</a>,
the <a href="http://landsat.usgs.gov" target="_blank" > U.S. Geological Survey (USGS) Landsat Satellite</a>,
the <a href="http://harvardforest.fas.harvard.edu/" target="_blank">Harvard Forest</a>,
and the <a href="https://www.census.gov/geo/maps-data/data/tiger-cart-boundary.html" target="_blank">US Census Bureau</a>

---

## License
This site uses the Minimal Mistakes these for Jekyll. The theme is open source
software
[GNU General Public License](http://mmistakes.github.io/minimal-mistakes/LICENSE)
version 2 or later.
