; ModuleID = 'constant_ops.ll'
source_filename = "constant_ops"

define i32 @test_const_add() {
entry:
  %add = add i32 5, 10
  ret i32 %add
}

define i32 @test_const_sub() {
entry:
  %sub = sub i32 20, 5
  ret i32 %sub
}
