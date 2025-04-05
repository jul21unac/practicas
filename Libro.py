class Libro:
    libros = []

    def __init__(self, titulo, autor, anio):
        self._titulo = titulo
        self._autor = autor
        self._anio = anio

        Libro.libros.append(self)
    @classmethod
    def mostrar_libros(cls):
        for  i in cls.libros:
            print(i)

    def __str__(self):
        return f'libro {self._titulo} de {self._autor} el anio ({self._anio})'

