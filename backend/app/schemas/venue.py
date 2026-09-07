from pydantic import BaseModel
class VenueCreate(BaseModel): nama:str; lokasi:str; latitude:float; longitude:float; jumlah_court:int; harga_sewa:float; jam_operasi:str; hari_operasi:str
class VenueOut(VenueCreate): id:str
