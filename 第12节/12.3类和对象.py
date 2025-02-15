class Clock:
    id = None
    price = None

    def ring(self):
        import winsound
        winsound.Beep(2000,3000)

clock1 = Clock()
clock1.id = '无始'
clock1.price = 10000
print(f'{clock1.id}钟，威力为：{clock1.price}')
clock1.ring()

clock2 = Clock()
clock2.id = '无终'
clock2.price = 8000
print(f'{clock2.id}钟，威力为：{clock2.price}')
clock1.ring()
