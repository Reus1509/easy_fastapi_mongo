from datetime import date

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from routes.user_routes import user
app = FastAPI()

app.include_router(user)










#
# @app.get("/hotels")
# async def get_hotels(location: str,
#                      date_from: date,
#                      date_to: date,
#                      stars: Optional[int] = None,
#                      has_spa: Optional[bool] = None,
#                      ):
#     return {"location": location,
#             "date_from": date_from,
#             "date_to": date_to,
#             }
#
# class SBooking(BaseModel):
#     room_id: int
#     date_from: date
#     date_to: date
#     price: float
#
#
#
# @app.post("/bookings")
# def add_booking(booking: SBooking):
#     return {"room_id": booking.room_id}