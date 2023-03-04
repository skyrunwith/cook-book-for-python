from chapter_12.example_10_Defining_an_actor_task import Actor


# Sample ActorTask
class PrintActor(Actor):
    def run(self):
        while True:
            msg = self.recv()
            print('Got: ', msg)


p = PrintActor()
p.start()
p.send('Hello')
p.send('World')
p.close()
p.join()
