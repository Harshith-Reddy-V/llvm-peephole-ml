; ModuleID = 'bitwise.ll'
source_filename = "bitwise"

define i32 @test_xor_zero(i32 %a) {
entry:
  %xor = xor i32 %a, 0
  ret i32 %xor
}

define i32 @test_and_minus_one(i32 %a) {
entry:
  %and = and i32 %a, -1
  ret i32 %and
}

define i32 @test_or_zero(i32 %a) {
entry:
  %or = or i32 %a, 0
  ret i32 %or
}
