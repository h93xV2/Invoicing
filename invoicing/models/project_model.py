from model_validation.field import Field
from model_validation.validations import IsString, IsInteger
from models.base_model import BaseModel


class ProjectModel(BaseModel):
    reference_code = Field([IsString()], nullable=True)
    date = Field([IsString()], nullable=True)
    client_id = Field([IsInteger()])  # Todo validate relation exists