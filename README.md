# energy-api

Demo API built with Python and the Django framework.

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

`plz=[integers]`

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

`plz=[integers]`

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

**Notes**
----

- Specification called for using a field termed 'yield.' This is a restricted keyword and I opted to use 'pv_yield' instead
- The original specification included supplying the 'plz' param instead of 'state' when performing the calculation. The specification was changed later, removing mention of 'plz' as a param, and instead using 'state' with 'capacity'. I've chosen to include use of the 'plz' param as an alternate feature (since I already had done the work to support it). I've noted above that 'plz' is an optional alternative to supplying the German state
