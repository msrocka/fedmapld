
import fedelemflowlist as fedfl
import pandas as pd
import olca


class Writer(object):

    def __init__(self, version=0.1, flow_list: pd.DataFrame = None,
                 flow_mapping: pd.DataFrame = None):

        if flow_list is None:
            self.flow_list = fedfl.get_flowlist(version)  # type: pd.DataFrame
        else:
            self.flow_list = flow_list

        if flow_mapping is None:
            self.flow_mapping = fedfl.get_flowmapping(  # type: pd.DataFrame
                version)
        else:
            self.flow_mapping = flow_mapping
