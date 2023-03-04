from chapter_12.example_10_Defining_an_actor_task import Actor


class TaggedActor(Actor):
    def run(self):
        while True:
            tag, *payload = self.recv()
            getattr(self, 'do_' + tag)(*payload)

    def do_A(self, x):
        print('Running A', x)

    def do_B(self, x, y):
        print('Running B', x, y)

        
p = TaggedActor()
p.start()
p.send(('A', 1))
p.send(('B', 'a', 'b'))
p.close()
p.join()