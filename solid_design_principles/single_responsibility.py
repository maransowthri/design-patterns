# Single Responsibility Principle (SRP) or Separation Of Concerns (SOC)
class Journal():
    def __init__(self):
        self.entries = []
        self.count = 0
    
    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')
    
    def remove_entry(self, index):
        self.count -= 1
        self.entries.pop(index)
    
    def __str__(self):
        return '\n'.join(self.entries)

    # def save(self, filename):
    #     with open(filename, 'w') as f:
    #         f.write(str(self))
    
    # def load(self):
    #     pass

    # def load_from_web(self):
    #     pass


class PersistanceManager:
    @staticmethod
    def save_to_file(filename, journal):
        with open(filename, 'w+') as f:
            f.write(str(journal))

journal = Journal()
journal.add_entry('I love programming')
journal.add_entry('I always ask right questions')
# journal.save('sample.txt')
print(journal)

PersistanceManager.save_to_file('sample.txt', journal)