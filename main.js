trophic_level = [20000, 1000, 100, 10];
repeats = 100;

for (i = 0; i < repeats; i++) {
  print_str = "";
  for (p = 0; p < trophic_level.length; p++) {
    print_str = print_str + trophic_level[p].toString() + ", ";
  }
  print_str = print_str.substring(0, print_str.length - 2);
  console.log(print_str);
  new_tl = Array.apply(null, Array(trophic_level.length)).map(Number.prototype.valueOf,0);
  new_tl[0] = 200000;
  for (p = 1; p < trophic_level.length; p++) {
    for (n = 0; n < trophic_level[p]; n++) {
      if (trophic_level[p] == 0)
        q_score = 0.001;
      else
        q_score = new_tl[p-1]/trophic_level[p];
      rand_score = Math.floor(Math.random() * 10);
      if (q_score > 10) {
        if (rand_score < 3) {
          new_tl[p]++;
          new_tl[p-1]--;
        } else {
          new_tl[p]+=2;
          new_tl[p-1]-=2;
        }
      } else if (q_score <= 10 && q_score > 1) {
        if (rand_score < 3) {
          new_tl[0] += 0.5;
        } else if (rand_score > 7) {
          new_tl[p]+=2;
          new_tl[p-1] -= 2;
        } else {
          new_tl[p]++;
          new_tl[p-1]--;
        }
      } else if (q_score <= 1 && q_score > 0) {
        if (rand_score < 2) {
          new_tl[p]++;
          new_tl[p-1]--;
        } else {
          new_tl[0] += 0.5;
        }
      }
    }
  }
  trophic_level = new_tl;
}
