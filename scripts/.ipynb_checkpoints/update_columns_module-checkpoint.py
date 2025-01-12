import arviz as az
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import seaborn.objects as so
import numpy as np
import pandas as pd
import polars as pl

import warnings
warnings.filterwarnings("ignore", category=UserWarning)

def update_columns(data_frame):
    unique_events = ['field_out', 'strikeout', 'walk', 'single', 'double', 'triple', 'home_run', 'force_out', 'grounded_into_double_play',
                    'hit_by_pitch', 'field_error','sac_fly']
    hit_events = ['single','double','triple','home_run']
    out_events = ['double_play', 'field_error','field_out','fielders_choice_out','force_out','grounded_into_double_play','other_out','strikeout',
                  'strikeout_double_play','triple_play']
    on_base_events = ['walk', 'hit_by_pitch','sac_fly','sac_bunt']

    data_frame['hit_n'] = 0
    data_frame['out_n'] = 0
    data_frame['ob_n'] = 0
    
    for event in unique_events:
        data_frame[f'{event}_n'] = data_frame.groupby(['batter', 'game_year'])['events'].transform(lambda x: (x == event).sum())
        
    for event in hit_events:
        data_frame['hit_n'] += data_frame.groupby(['batter','game_year'])['events'].transform(lambda x: (x == event).sum())
    for event in out_events:
        data_frame['out_n'] += data_frame.groupby(['batter','game_year'])['events'].transform(lambda x: (x == event).sum())
    for event in on_base_events:
        data_frame['ob_n'] += data_frame.groupby(['batter','game_year'])['events'].transform(lambda x: (x == event).sum())
        
    data_frame['n_pitches'] = data_frame.groupby(['batter','game_year'])['events'].transform('size')
    data_frame['total_events'] = data_frame['hit_n'] + data_frame['out_n'] + data_frame['ob_n']

    return data_frame