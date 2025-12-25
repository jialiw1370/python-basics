
def skincare(i):
  """Return a short explanation for a skincare ingredients.
Args:
    ingredient: Name of the ingredient (str)

Returns:
    Explanation string if known, otherwise None.
  """
  if i == "Vitamin C":
    return "Vitamin C brightens your skin"
  if i == "Retinol":
    return "Retinol reduces your wrinkles"
  if i == "Hyaluronic Acid":
    return "Hyaluronic Acid moisturizes your skin"
  if i == "Niacinamide":
    return "Niacinamide brightens your skin"
  else:
    return "Try again! Try typing 'Vitamin C', 'Retinol' etc"

skincare("youself")
