from fastapi import APIRouter
router = APIRouter(prefix='/shipments')

@router.post('')
async def create_shipment() -> dict:
    """Create a new shipment."""
    return {}

@router.get('/{shipment_id}')
async def get_shipment(shipment_id: int) -> dict:
    """Fetch a single shipment."""
    return {}

@router.patch('/{shipment_id}')
async def update_shipment(shipment_id: int) -> dict:
    """Update an existing shipment."""
    return {}

@router.delete('/{shipment_id}', status_code=204)
async def delete_shipment(shipment_id: int) -> None:
    """Delete an existing shipment."""
    pass