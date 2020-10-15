# Cupcake_API

An API where you can add/edit/delete cupcakes, and view all (or a specific) cupcake(s).

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install from requirement.txt.

```bash
pip install -r requirements.txt 
```

## Usage

```python

GET '/api/cupcakes' - returns JSON about all cupcakes.

POST '/api/cupcakes' - include flavor,size,rating and image url(optional) to create cupcake and returns JSON about cupcake.

GET '/api/cupcakes/cupcake-id' - returns JSON about a specific cupcake.

PATCH '/api/cupcakes/cupcake-id' - include flavor,size,rating and image url(optional) to update cupcake and returns JSON about cupcake.

DELETE '/api/cupcakes/cupcake-id' - deletes specific cupcake and returns JSON advising cupcake has been deleted.

```

