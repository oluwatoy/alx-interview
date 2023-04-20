#!/usr/bin/python3

function pascal(rows) {
  if (rows === 1) {
    return [[1]];
  }
if (rows === 0) {
    return [];
  }
  const prev = pascal(rows - 1);
  const last = prev[prev.length - 1];
  const next = [1];
  for (let i = 0; i < last.length - 1; i++) {
    next.push(last[i] + last[i + 1]);
  }
  next.push(1);
  prev.push(next);
  return prev;
}
