wget http://www.cpc.ncep.noaa.gov/products/analysis_monitoring/ocean/index/heat_content_index.txt
wget ftp://ftp.bom.gov.au/anon/home/ncc/www/sco/soi/soiplaintext.html > SOI.txt
mkdir Dir_PacificoSur
mv heat_content-index.txt SOI.txt PCA_PacificoSur.py ../Dir_PacificoSur
cd Dir_PacificoSur
python PCA_PacificoSur.py

