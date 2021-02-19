import re


''' 
    In order to avoid regex, we can execute several split 
    and iterate the list through incompatibles.
'''


def valid_email(mail):

    try:
        1/len(re.compile(
            r'^[A-z0-9][A-z._%+-]{1,}@{1}(?:[A-z](?:[A-z]|[^-_@]{0,}[A-z])?\.){1,}[A-z]{2,}$'
        ).findall(mail))
        return 'Email is valid'
    except ZeroDivisionError:
        return 'Email is not valid'


# check_tests:
# print(valid_email("trafik@cz.media.net")) # 1 #ok
# print(valid_email("trafik@cz.media.n0t")) # 0 #ok False
# print(valid_email("t@i.f.not")) # 1 #ok
# print(valid_email("t@i.f0f_not")) #ok False
# print(valid_email("t@i.f0f.not")) # ok False
# print(valid_email("t@i.f0f-not")) # ok False
# print(valid_email("t@i.fu..not")) # ok False


# Function example:
# tests Soft serve:
# print(valid_email("trafik@ukr.tel.com"))  # output:   "Email is valid"
# print(valid_email("trafik@ukr_tel.com"))  # output:   "Email is not valid"
# print(valid_email("tra@fik@ukr.com"))  # output:   "Email is not valid"
# print(valid_email("ownsite@our.c0m"))  # output:   "Email is not valid"
# print(valid_email("example@source.ua"))  # output: "Email is valid"


# print(valid_email("probaggdf@gmail.hhh.com")) # Email is valid
# print(valid_email("example@source_arth.com")) # Email is not valid
# print(valid_email("exam@ple@sourcepath.com")) # # Email is not valid
# print(valid_email("examplesource_arth.com")) ## Email is not valid
# print(valid_email("example@source.ua")) ## Email is valid

