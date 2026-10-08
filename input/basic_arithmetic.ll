; ModuleID = 'basic_arithmetic.ll'
source_filename = "basic_arithmetic"

define i32 @test_add_zero(i32 %a) {
entry:
  %add = add i32 %a, 0
  ret i32 %add
}

define i32 @test_sub_zero(i32 %a) {
entry:
  %sub = sub i32 %a, 0
  ret i32 %sub
}

define i32 @test_mul_one(i32 %a) {
entry:
  %mul = mul i32 %a, 1
  ret i32 %mul
}
