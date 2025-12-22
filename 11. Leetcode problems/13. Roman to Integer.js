/**
 * @param {string} s
 * @return {number}
 */

 const rom_int_map = {
  I: 1,
  V: 5,
  X: 10,
  L: 50,
  C: 100,
  D: 500,
  M: 1000,
};
// const ending_high_value_symbols = ["V", "X", "L", "C", "D", "M"];

var romanToInt = function (s) {
  let final_value = 0;

  for (let curr_sym = 0; curr_sym <= s.length - 1; curr_sym++) {
    const next = rom_int_map[s[curr_sym + 1]]
    const now = rom_int_map[s[curr_sym]]
    if (
     next &&
      now < next
    ) {
      final_value += next - now;
      curr_sym++;
    } else {
      final_value += now;
    }
  }
  return final_value;
};