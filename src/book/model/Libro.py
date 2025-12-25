class Libro:
    libros = []

    def __init__(self, titulo, autor, anio, genero):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.genero = genero

        Libro.libros.append(self)

    @property
    def genero(self):
        return self._genero
    @genero.setter
    def genero(self,value):
        self._genero = value


    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self,value):
        self._titulo = value

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self,value):
        self._autor =value

    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self,value):
        self._anio = value



    @classmethod
    def mostrar_libros(cls):
        for  i in cls.libros:
            print(i)

    def __str__(self):
        return f'libro {self._titulo} de {self._autor} el anio ({self._anio})'


