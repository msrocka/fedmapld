
import os
import logging as log

import fedelemflowlist as fedfl
import pandas as pd
import olca
import olca.pack as pack


class Writer(object):

    def __init__(self, version="0.1", flow_list: pd.DataFrame = None,
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

    def write_to(self, path: str):
        if os.path.exists(path):
            os.remove(path)
        pw = pack.Writer(path)
        self._write_top_categories(pw)
        self._write_flow_compartments(pw)
        pw.close()

    def _write_top_categories(self, pw: pack.Writer):
        # elementary flows
        root = olca.Category()
        root.id = "f318fa60-bae9-361f-ad5a-5066a0e2a9d1"
        root.name = "Elementary flows"
        root.model_type = olca.ModelType.FLOW
        pw.write(root)

        # resources
        res = olca.Category()
        res.id = "3095c63c-7962-4086-a0d7-df4fd38c2e68"
        res.name = "resource"
        res.category = olca.ref(olca.Category, root.id)
        res.model_type = olca.ModelType.FLOW
        pw.write(res)

        # emissions
        emi = olca.Category()
        emi.id = "c2433915-9ca3-3933-a64d-68d67e3e3281"
        emi.name = "emission"
        emi.category = olca.ref(olca.Category, root.id)
        emi.model_type = olca.ModelType.FLOW
        pw.write(emi)

    def _write_flow_compartments(self, pw: pack.Writer):
        handled = set()
        i = 0
        for _, row in self.flow_list.iterrows():
            uid = row[12]
            if uid in handled:
                continue
            handled.add(uid)
            parent_uid = None
            direction = row[6].strip()
            if direction == "resource":
                parent_uid = "3095c63c-7962-4086-a0d7-df4fd38c2e68"
            elif direction == "emission":
                parent_uid = "c2433915-9ca3-3933-a64d-68d67e3e3281"
            else:
                log.error("Unknown directionality: %s", direction)
                continue
            comp = olca.Category()
            comp.id = uid
            comp.name = row[7]
            comp.model_type = olca.ModelType.FLOW
            comp.category = olca.ref(olca.Category, parent_uid)
            pw.write(comp)

    def _write_flows(self, pw: pack.Writer):
        pass
