# HKT data
These lines of code allow downloading all details of PCCW/HKT Netvigator Broadband, NowTV and Business Netvigator coverage.

I wanted to find an easy way to check for coverage before moving houses.

### JSON file layout
The JSON file looks like this:

```json
{
        "AREA_CD": "HK",
        "BUILD_XY": "3591815263",
        "BUS_BASIC_BW": "8",
        "BUS_FTTB_BW": "100",
        "BUS_FTTH_BW": "1000",
        "BUS_TV_HD": "Y",
        "BUS_TV_SD": "Y",
        "BUS_TV_SUPER_HD": "N",
        "DISTR_CD": "106",
        "IS_HOS": "N",
        "IS_PH": "N",
        "IS_PREMIER": "N",
        "IS_RM": "N",
        "NAME_CH": "其發大廈",
        "NAME_EN": "LUCKIFAST BUILDING",
        "RES_BASIC_BW": "8",
        "RES_FTTB_BW": "100",
        "RES_FTTH_BW": "10000",
        "RES_TV_HD": "Y",
        "RES_TV_SD": "Y",
        "RES_TV_SUPER_HD": "Y",
        "SECT_CD": "ZZZZ",
        "SF_BLDG_BUS": "N",
        "SF_BLDG_RES": "Y",
        "SITE_GROUP": "99",
        "STREET_NAME_CH": "石水渠街",
        "STREET_NAME_EN": "STONE NULLAH LANE",
        "STREET_NUM": "1",
        "area_desc_ch": "香港",
        "area_desc_en": "HONG KONG",
        "district_desc_ch": "灣仔",
        "district_desc_en": "WAN CHAI",
        "housing_addr_ch": "石水渠街1號其發大廈",
        "housing_addr_en": "LUCKIFAST BUILDING, 1 STONE NULLAH LANE",
        "lat": "22.276224",
        "lng": "114.17348",
        "marker_idx": "97248"
    }
```

#### Residential
```
"RES_BASIC_BW": "8"     --> 8 Mbit/s DSL available
"RES_FTTB_BW": "100"    --> 100 Mbit/s Fibre-To-The-Building (?!) available
"RES_FTTH_BW": "10000"  --> 10 Gbit/s Fibre-To-The-Building available
"RES_TV_HD": "Y"        --> HD TV available
"RES_TV_SD": "Y"        --> SD TV available
"RES_TV_SUPER_HD": "Y"  --> TV Super HD available
```
#### Business
```
"BUS_BASIC_BW": "8"     --> 8 Mbit/s DSL available
"BUS_FTTB_BW": "100"    --> 100 Mbit/s Fibre-To-The-Building (?!) available
"BUS_FTTH_BW": "1000"   --> 1 Gbit/s Fibre-To-The-Home available
"BUS_TV_HD": "Y"        --> HD TV available
"BUS_TV_SD": "Y"        --> SD TV available
"BUS_TV_SUPER_HD": "N"  --> TV Super HD not available
```