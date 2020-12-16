# energy-api
**kWh/kWp**
----
Fetches one kWh/kWp pv_yield when DE state or plz is provided.

### URL

`/api/pv_yield/`

### Method

`GET`

### URL Params

#### Required

`state=[characters]`

- Two characters required
- One of sixteen German states

*Alternatively Replace State With*

`plz=[integer]`

- Five digits required
- German postal code value

### Success Response

- Code: `200`
- Content: `{"pv_yield" : 1100, "state" : "sl"}`

### Error Response

- Code: `404`
- Content: `"detail": "Not found."`

### Sample Calls

- State param

`https://de-energy.herokuapp.com/api/pv_yield?state=sl`

- Postal Code param

`https://de-energy.herokuapp.com/api/pv_yield?plz=08606`

**kWh/year**
----
Calculates one kWh/year pv_yield when capacity (kWp) and DE state or plz is provided.

### URL

`/api/pv_yield/`

### Method

`GET`

### URL Params

#### Required

`capacity=[integers]`

`state=[characters]`

- Two characters required
- One of sixteen German states

*Alternatively Replace State With*

`plz=[integer]`

- Five digits required
- German postal code value

### Success Response

- Code: `200`
- Content: `{"pv_yield" : 11000, "state" : "sl"}`

### Error Response

- Code: `404`
- Content: `"detail": "Not found."`

### Sample Calls

- State param

`https://de-energy.herokuapp.com/api/pv_yield?state=sl&capacity=10`

- Postal Code param

`https://de-energy.herokuapp.com/api/pv_yield?plz=08606&capacity=10`
