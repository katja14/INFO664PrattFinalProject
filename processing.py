

#def get_percent_social(stateDf):
#    # go through each row in my state chart
#        # in each row, check if values in SM columns are 0 or 1
#        # if" at least 1 has a 1, increase your "has social media" counter
#    # return "has social media" counter divided by the length of the chart 
#    libraries = len(stateDf)
#    
#    len(stateDf.loc[stateDf['facebook.com']== 1.0]) > 0 or 
#    len(stateDf.loc[stateDf['twitter.com']== 1.0]) > 0 or 
#    len(stateDf.loc[stateDf['youtube.com']== 1.0]) > 0 or len(stateDf.loc[stateDf['instagram.com']== 1.0]) > 0 or len(stateDf.loc[stateDf['nextdoor.com']== 1.0]) > 0 or len(stateDf.loc[stateDf['linkedin.com']== 1.0]) > 0

import pandas
def process_by_state():
    df = pandas.read_json("all_libraries_with_sites.json")
    # look at data by state
    state_list = df.state.unique()

    for state in state_list:
        # use .loc to look at the data by state
        stateDf = df.loc[df['state'] == state]

        fb = stateDf.loc[stateDf['facebook.com']== 1.0]
        percent_fb = len(fb)/len(stateDf)
        print(len(fb), 'out of', len(stateDf), 'libraries in', state, 'use Facebook.')
        
        tw = stateDf.loc[stateDf['twitter.com']== 1.0]
        percent_tw = len(tw)/len(stateDf)
        print(len(tw), 'out of', len(stateDf), 'libraries in', state, 'use Twitter.')

        ig = stateDf.loc[stateDf['instagram.com']== 1.0]
        percent_ig = len(tw)/len(stateDf)
        print(len(ig), 'out of', len(stateDf), 'libraries in', state, 'use Instagram.')

        yt = stateDf.loc[stateDf['youtube.com']== 1.0]
        percent_yt = len(tw)/len(stateDf)
        print(len(yt), 'out of', len(stateDf), 'libraries in', state, 'use YouTube.')
        
        li = stateDf.loc[stateDf['linkedin.com']== 1.0]
        percent_li = len(li)/len(stateDf)
        print(len(li), 'out of', len(stateDf), 'libraries in', state, 'use LinkedIn.')
        
        nd = stateDf.loc[stateDf['nextdoor.com']== 1.0]
        percent_nd = len(nd)/len(stateDf)
        print(len(nd), 'out of', len(stateDf), 'libraries in', state, 'use Nextdoor.')
        #percent_social = get_percent_social(stateDf)

        # what percent of libraries in the state have social media?
        # do libraries in the state have facebook?
        # do libraries in the state have instagram?
        # do libraries in the state have youtube?
        # twitter?

process_by_state()
    
