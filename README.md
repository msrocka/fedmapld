# fedmapld
`fedmapld` generates JSON-LD packages including flow mappings from the
[Federal LCA Commons Elementary Flow List](https://github.com/USEPA/Federal-LCA-Commons-Elementary-Flow-List).
If this works well this could be integrated into the flow lists repository.

## Usage

```bash
# checkout this repository
git clone https://github.com/msrocka/fedmapld.git
cd fedmapld

# create a virtual environment and install the dependencies
python -m venv env
./env/Scripts/activate
pip install -r requirements.txt

# install the current version of the Fed.LCA Flow-List
pip install git+https://github.com/USEPA/Federal-LCA-Commons-Elementary-Flow-List.git@master

# install this module
pip install -e .

```
