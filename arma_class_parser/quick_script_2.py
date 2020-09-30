from gidtools.gidfiles import get_pickled, writejson


a = get_pickled("D:/Dropbox/hobby/Modding/Programs/Github/My_Repos/Arma_class_parser_utility/arma_class_parser/all_config_dump_rhs_ace_3cb.pkl")
writejson(a, 'all_config_dump_rhs_ace_3cb.json')
