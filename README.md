# Marshmallow JSON API Webargs

## Installation
```bash
pip install marshmallow-jsonapi-webargs
```

## Usage
Create a parser that adds in an improved query string logic:
```python
import marshmallow_jsonapi_webargs as jaw
from webargs.flaskparser import FlaskParser

class FlaskJsonApiParser(jaw.NestedQueryParserMixin, FlaskParser):
    pass
parser = FlaskJsonApiParser()
```

Create the schema using some combination of the provided fields, according to which fields your API supports:
```python
from marshmallow import Schema
import marshmallow_jsonapi_webargs as jaw

class JsonApiRequestSchema(Schema):
    sort = jaw.Sort()
    include = jaw.Include()
    fields = jaw.Fields()
    page = jaw.PagePagination()
    filter = jaw.Filter()
```

Use the schema to define your request format
```python
@parser.use_args(JsonApiRequestSchema())
def greet(args):
    return 'You requested to include these relationships: ' + ', '.join(args['include'])
```

## Tests
To run the tests:

* Clone the repo: 
    ```
    git clone git@github.com:TMiguelT/marshmallow-jsonapi-webargs.git
    cd marshmallow-jsonapi-webargs
    ```
* Install the test dependencies:
    ```bash
    pip install '.[dev]'
    ```
* Run the tests:
    ```bash
    pytest test.py
    ```
