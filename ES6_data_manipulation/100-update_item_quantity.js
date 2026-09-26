export default function updateQuantityOfMapItem(map, initialAttribute, newQuantity) {
  if (!map.has(initialAttribute)) {
    throw new Error('Cannot update it');
  }
  map.set(initialAttribute, newQuantity);
  return map;
}
