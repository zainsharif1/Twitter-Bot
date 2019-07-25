def word_prompt():
    """
    Creates a list of user provided names of agriculture products to be used
    as input to the tweet bot for locating tweets.

    If user wishes not to input anything (hits enter), then the default list
    provided below will be used.

    Inputs: None
    Returns (str): list

    """

    user_prompt = input(
    """
    Please enter agriculture keywords separated by comma to track in twitter:
    (Hit enter bar to quit and use default list)
    """)

    if len(str(user_prompt))<1:
        prompt_list = ['#wheat','#veg','#vegoil','#corn','#maize','#grain','#soy','#soybean','#oat']
    else:
        prompt_list = ["#"+str(prompt.lower().strip()) for prompt in user_prompt.split(",")]

    return prompt_list

def geo_area():
    """
    Creates a list of user provided names of countries to be used
    as input to the tweet bot for following tweets by certain geographical location.

    If user wishes not to input anything (hits enter), then the default dictionary
    provided below will be used.

    Inputs: None
    Returns (str): list (user provided) or dict(default)

    """

    user_prompt = input(
    """
    \n
    Please enter country separated by comma to track in twitter:
    (Hit enter bar to quit and use default list)
    """)



    if len(str(user_prompt))<1:
        #create a dictionary of continents and countries and use 'Europe' list as default
        geo_dict ={'Europe': ['Switzerland','Germany','Italy','France','United Kingdom'],'Asia':['Japan','China','India','Hong Kong'],'Latin America':['Brazil','Argentina','Venezuela'],'North America':['United States','Canada','Mexico']}
        geo_area = geo_dict['Europe']
    else:
        geo_area = [prompt.lower().strip() for prompt in user_prompt.split(",")]

    return geo_area
