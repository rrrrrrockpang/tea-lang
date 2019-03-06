import tea
import os

base_url = 'https://homes.cs.washington.edu/~emjun/tea-lang/datasets/'
uscrime_data_path = None

def test_load_data():
    global base_url, uscrime_data_path

    csv_name = 'UScrime.csv'
    csv_url = os.path.join(base_url, csv_name)
    uscrime_data_path = tea.download_data(csv_url, 'UScrime')

def test_indep_t_test():
    global uscrime_data_path

    # Declare and annotate the variables of interest
    # is_south = nominal('So', ['0', '1'])
    # probability = ratio('Prob', drange=[0,1])
    # variables = [is_south, probability]
    variables = [
        {
            'name' : 'So',
            'data type' : 'nominal',
            'categories' : ['0', '1']
        },
        {
            'name' : 'Prob',
            'data type' : 'ratio',
            'range' : [0,1]
        }
    ]
    experimental_design = {
                            'study type': 'observational study',
                            'contributor variables': 'So',
                            'outcome variables': 'Prob',
                        }
    assumptions = {
        'Type I (False Positive) Error Rate': 0.05
    }

    tea.data(uscrime_data_path)
    tea.define_variables(variables)
    tea.define_study_design(experimental_design) # Allows for using multiple study designs for the same dataset (could lead to phishing but also practical for saving analyses and reusing as many parts of analyses as possible)
    tea.assume(assumptions)
    tea.hypothesize(['So', 'Prob'])
    # Can always redefine experimental design 
    # tea.define_study_design(experimental_design)

    # Separate out the unique participant_id from loading_data to experimental design
    # --> This means that need to update Dataset object 
    

    # Don't want to call AST builder here do we? Could create separate API for user
    
    # Need to make sure that we are calling/hooking into solver in evaluation of Relate...

    # What happens when have no participant_id?
    # --> ask for key
    # ---> if there is no key, assume that each row is a separate/unique participant/observation 
    # --> May want to surface this assumption to the user....
    # dataset = tea.load_data(uscrime_data_path, variables, 'participant_id')

    
    import pdb; pdb.set_trace()
    # ds = load_data(file_path, variables, 'participant_id')