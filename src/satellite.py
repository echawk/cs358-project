from t import *

class Satellite:
    sat_id: str = ""
    normad: int = 0
    name: str = ""
    names: List[str] = []
    image: str = ""
    status: str = ""
    is_alive: bool = False
    is_decayed: bool = False
    is_launched: bool = False
    is_deployed: bool = False
    website: str = ""
    operator: str = ""
    countries: List[str] = []
    telemetries: List[str] = []
    updated: str = ""
    citation: str = ""
    associated_satellites: List[str] = []


    def __init__(self):
        assert False, "Satellite.__init__() not implemented yet"
