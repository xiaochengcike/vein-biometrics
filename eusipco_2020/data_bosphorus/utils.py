"""
This code is generated by Ridvan Salih KUZU @UNIROMA3
LAST EDITED:  01.04.2020
ABOUT SCRIPT:
It is a script for utility functions used in Bosphorus Package.
"""

import torch
import pandas as pd
from utils import feature_binarizer

def feature_exporter(main_model, encoder_model, data_loader, output_file=None):
    df_features = pd.DataFrame()
    df_header = pd.DataFrame()

    with torch.set_grad_enabled(False):
        main_model.eval()
        for batch_idx, (data, target, file_name) in enumerate(data_loader):
            output = main_model(data, False)
            #output = feature_binarizer(output)
            for t,f,o in zip(target,file_name,output):
                df_features = df_features.append(pd.Series(o.data.cpu().numpy(),name=str(int(t.data.cpu().numpy()))),ignore_index=True)
                df_header = df_header.append({'file_name': f, 'class': t.data.cpu().numpy().tolist()},ignore_index=True)

        if output_file is not None:
            result = df_header.join(df_features,how='inner')
            result = result.sort_values(by=['class']).reset_index(drop=True)
            result.to_csv(output_file, index=False)
        else:
            return df_features.values
