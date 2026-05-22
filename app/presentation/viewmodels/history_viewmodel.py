from collections import defaultdict

from app.infrastructure.repositories.sqlite_water_intake_repository import (
  SqliteWaterIntakeRepository,
)


class HistoryViewModel:
  def __init__(self):
    self._repository = SqliteWaterIntakeRepository()

  def get_all(self):
    return self._repository.get_all()

  def get_grouped_by_day(self) -> list[dict]:
    items = self._repository.get_all()

    grouped = defaultdict(list)

    for item in items:
      date_key = item.created_at.date()
      grouped[date_key].append(item)

    result = []

    for date_key, day_items in grouped.items():
      total_ml = sum(item.amount_ml for item in day_items)

      result.append({
        "date": date_key,
        "total_ml": total_ml,
        "items": day_items,
      })

    result.sort(
      key=lambda item: item["date"],
      reverse=True,
    )

    return result

  def delete_by_id(self, water_intake_id: int) -> bool:
    return self._repository.delete_by_id(water_intake_id)

  def update_amount(self, water_intake_id: int, amount_ml: int) -> bool:
    if amount_ml <= 0:
      raise ValueError("A quantidade deve ser maior que zero.")

    if amount_ml > 5000:
      raise ValueError("A quantidade máxima permitida é 5000 ml.")

    return self._repository.update_amount(water_intake_id, amount_ml)