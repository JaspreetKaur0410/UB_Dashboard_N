from configparser import ConfigParser

def dbConfig(section,filename='.streamlit/secrets.toml'):
    parser=ConfigParser()
    parser.read(filename)
    print("*********************************************************************")
    print(section)

    db={}
    # check if section is available in secrets.toml
    if parser.has_section(section):
        params=parser.items(section)
        for each_param in params:
            str_param=each_param[1]
            if each_param[0]=="port":
                db[each_param[0]]=int(str_param)
            else:
                db[each_param[0]]=str_param[1:len(str_param)-1]
    elif parser.has_section('AZURE'):
        params=parser.items('AZURE')
        for each_param in params:
            str_param=each_param[1]
            if each_param[0]=="port":
                db[each_param[0]]=int(str_param)
            else:
                db[each_param[0]]=str_param[1:len(str_param)-1]
    else:
        raise Exception('Section is not Found')
    # converting port to integer
    for d in db:
        if d=="port":
            db[d]=int(db[d])
    return db