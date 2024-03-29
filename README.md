# fedmapld
`fedmapld` generates JSON-LD packages including flow mappings from the
[Federal LCA Commons Elementary Flow List](https://github.com/USEPA/Federal-LCA-Commons-Elementary-Flow-List).
If this works well this could be integrated into the flow lists repository.

## Usage
Currently, the best way to use this module is in a
[virtual environment](https://docs.python.org/3/library/venv.html):

```bash
# checkout this repository
git clone https://github.com/msrocka/fedmapld.git
cd fedmapld

# create a virtual environment and install the dependencies
python -m venv env
./env/Scripts/activate
pip install -r requirements.txt

# install the branch `flowmappingforolca` from the
# Fed.LCA Flow-List list repository
pip install git+https://github.com/USEPA/Federal-LCA-Commons-Elementary-Flow-List.git@flowmappingforolca

# install this module
pip install -e .

# then start the Python interpreter
python
```

The entry point of the JSON-LD export is the `fedmapld.jsonld.Writer`:

```python
>>> import fedmapld.jsonld as jsonld
>>> writer = jsonld.Writer()
```

This will internally load the default version of the Fed.LCA flow list and
mapping files (currently for version `0.1`). Alternatively, you can pass in
another version into the constructor of the writer (but currently only version
`0.1` works):

```python
>>> import fedmapld.jsonld as jsonld
>>> writer = jsonld.Writer(version="0.1")
```

Also, you can directly pass the flow list and mapping files as
[pandas data frames](https://pandas.pydata.org/pandas-docs/version/0.23.4/generated/pandas.DataFrame.html)
into the constructor (see the data format definition below):

```python
>>> writer = jsonld.Writer(flow_list=a_flow_list_df,
>>>                        flow_mapping=a_flow_mapping_df)
```

Finally, writing the JSON-LD package is done by calling the
`write_to` method on the writer which takes the path to the
resulting zip file as argument:

```python
>>> writer.write_to("path/to/file.zip")
```

## Data format
The flow list is a pandas data frame with the following columns:

```
Index   Label
-----   -------------------
  0     Flowable                - the flow name
  1     CAS No                  - CAS number
  2     Formula                 - chemical formula
  3     Synonyms                - flow synonyms
  4     Flow quality            - ! the reference *quantity* (e.g. Energy, Mass)
  5     Unit                    - the reference unit
  6     Directionality          - resource | emission
  7     Compartment             - air | ground | water ...
  8     External reference      - e.g. a web link
  9     Preferred               - 1 | 0
 10     Class                   - Energy | Fuel | ...
 11     Flow UUID
 12     Compartment UUID
 13     Unit UUID
 14     Quality UUID            - ! UUID of the quantity (flow property)
```

The mapping data frame should have the
[following columns](https://github.com/USEPA/Federal-LCA-Commons-Elementary-Flow-List/blob/master/format%20specs/FlowMapping.md):

```
 0  SourceListName
 1  SourceListVersion
 2  SourceFlowName
 3  SourceFlowUUID
 4  SourceFlowContext
 5  SourceUnit
 6  MatchCondition
 7  ConversionFactor
 8  TargetFlowName
 9  TargetFlowUUID
10  TargetFlowContext
11  TargetUnit
12  Mapper
13  Verifier
14  LastUpdated
```

## License
This project is in the worldwide public domain, released under the
[CC0 1.0 Universal Public Domain Dedication License](https://creativecommons.org/publicdomain/zero/1.0/).

![Public Domain Dedication](https://licensebuttons.net/p/zero/1.0/88x31.png)
