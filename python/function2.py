#def stundent_info(*args,**kwarts):
 #   print(args)
#    print(kwarts)
#stundent_info('maths','arts',name='john',age=23)
def stundent_info(*args,**knowldge):
    print(args)
    print(knowldge)
courses = ['maths','arts']
info = {'name' : 'john' ,'age' : 23}
stundent_info(*courses,**info)
