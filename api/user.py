import os

from common.YamlUtil import YamlUtil
from core.rest_client import RestClient

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "env.yml")
api_root_url = YamlUtil().read_yaml(data_file_path).get('zhicall_url')


class User(RestClient):

    def __init__(self, api_root_url, **kwargs):
        super(User, self).__init__(api_root_url, **kwargs)

    # def wechatAppletsLogin(self,  **kwargs):
    #     url = self.api_root_url + "/user-center/account/wechatAppletsLogin"
    #     return self.post(url, **kwargs)

    def PatientList(self, **kwargs):
        url = self.api_root_url + "/user-center/patient.listFilter.hsr"
        return self.post(url, **kwargs)


    # def list_all_users(self, **kwargs):
    #     return self.get("/users", **kwargs)
    #
    # def list_one_user(self, username, **kwargs):
    #     return self.get("/users/{}".format(username), **kwargs)
    #
    # def register(self, **kwargs):
    #     return self.post("/register", **kwargs)
    #
    # def login(self, **kwargs):
    #     return self.post("/login", **kwargs)
    #
    # def update(self, user_id, **kwargs):
    #     return self.put("/update/user/{}".format(user_id), **kwargs)
    #
    # def delete(self, name, **kwargs):
    #     return self.post("/delete/user/{}".format(name), **kwargs)


user = User(api_root_url)