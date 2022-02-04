person0 = {
    "first":"Mike",
    "last":"M",
    "food":["pizza","pasta","taco","ice cream","chicken"],
}
for p in person0:
    if type(person0[p]) is list:
        print(p)
        for l in person0[p]:
            print("\t",l)
    else:
        print(p,":",person0[p])