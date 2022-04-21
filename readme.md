Nous avons travailler avec les technologies suivantes :

- Microsoft Azure
- Python
- Flask
- React
- React-Leaflet


Ce projet récupère les données du traffic aérien de l'API d'[Airlabs](https://airlabs.co/) et les stock en base de données pour ensuite les afficher sur une couche cartographique web. 

Notre base de données **rtap** est constitué de deux tables **plane** & **flight**


**plane**

| name of column | type of value |
| --- | --- |
| reg_number  | int(11) |
| aircraft_icao | varchar(255) |



**flight**

| name of column | type of value |
| --- | --- |
| id  | int(11) |
| flight_icao | varchar(255) |
| airline_icao | varchar(255) |
| status | varchar(255) |



<details><summary>CLICK ME</summary>
<p>

#### We can hide anything, even code!

    ```ruby
      puts "Hello World"
    ```

</p>
</details>
