# Import, Update, and Explore

* Write a command that imports the data from [annual_aqi_by_county_2022.csv](../Resources/annual_aqi_by_county_2022.csv) to a database called `epa` and a collection called `annual_aqi_by_county`. If the collection already exists, drop the collection.

* Write a command that imports the data from [ohio_daily_records_2022.json](../Resources/ohio_daily_records_2022.json) to a database called `epa` and a collection called `ohio_daily_records`. If the collection already exists, drop the collection.

* Write a command that imports the data from [ohio_jan_2022.json](../Resources/ohio_jan_2022.json) to a database called `epa` and a collection called `ohio_air`. If the collection already exists, drop the collection.

* Write a command that imports the data from [ohio_feb_2022.json](../Resources/ohio_feb_2022.json) to a database called `epa` and a collection called `ohio_air`. **Note:** This is the same collection used in the previous import so be sure not to drop the collection in advance.

* Use the `epa` database.

* Show all the collections in the `epa` database.

* Verify that there is data in each of the 3 collections (`ohio_daily_records`, `annual_aqi_by_county`, and `ohio_air`) by using `findOne()` to display an entry.

* Verify that there is data from January 2022 in the `ohio_air` collection by seaching on the `date_local` field.

* Verify that there is data from February 2022 in the `ohio_air` collection by seaching on the `date_local` field.

* Update the `DAILY_AQI_VALUE` nested under `CO` in the `ohio_daily_records` collection to change the string values to integers.

* Update the `PERCENT_COMPLETE` nested under `CO` in the `ohio_daily_records` collection to change the string values to doubles.

* Find a record in the `ohio_daily_records` collection where `CO.UNITS` matches "ppm" and `NO2.UNITS` matches "ppb"
