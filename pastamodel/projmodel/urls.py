from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from appmodelo.views.HomeViews import home
from appmodelo.views.GeneroViews import lista_generos, detalhes_genero, novo_genero, editar_genero, deletar_genero
from appmodelo.views.EditoraViews import lista_editoras, detalhes_editora, nova_editora, editar_editora, deletar_editora
from appmodelo.views.AutorViews import lista_autores, detalhes_autor, novo_autor, editar_autor, deletar_autor
from appmodelo.views.LivroViews import lista_livros, detalhes_livro, novo_livro, editar_livro, deletar_livro, livros_recentes, gerar_pdf_livro
from appmodelo.views.ExemplarViews import lista_exemplares, detalhes_exemplar, novo_exemplar, editar_exemplar, deletar_exemplar
from appmodelo.views.FuncionarioViews import lista_funcionarios,detalhes_funcionario, novo_funcionario, editar_funcionario, deletar_funcionario
from appmodelo.views.UsuarioViews import lista_usuarios, detalhes_usuario, novo_usuario, editar_usuario, deletar_usuario
from appmodelo.views.EmprestimoViews import lista_emprestimos, detalhes_emprestimo, novo_emprestimo, editar_emprestimo, deletar_emprestimo
from appmodelo.views.MultaViews import lista_multas, detalhes_multa, nova_multa, editar_multa, deletar_multa
from appmodelo.views.ComentarioViews import lista_comentarios, detalhes_comentario, novo_comentario, editar_comentario, deletar_comentario
from appmodelo.views.AvaliacaoViews import lista_avaliacoes, detalhes_avaliacao, nova_avaliacao, editar_avaliacao, deletar_avaliacao
from appmodelo.views.FuncLivroViews import lista_func_livros, detalhes_func_livro, novo_func_livro, editar_func_livro, deletar_func_livro
from appmodelo.views.ReservaViews import lista_reservas, detalhes_reserva, nova_reserva, editar_reserva, deletar_reserva
from appmodelo.views.LogsViews import lista_logs, detalhes_log, novo_log, editar_log, deletar_log

   
urlpatterns = [
    path('', home, name='home'),
    # URLs para o modelo Genero
    path('generos/', lista_generos, name='lista_generos'),
    path('genero/<int:pk>/', detalhes_genero, name='detalhes_genero'),
    path('genero/novo/', novo_genero, name='novo_genero'),
    path('genero/editar/<int:pk>/', editar_genero, name='editar_genero'),
    path('genero/deletar/<int:pk>/', deletar_genero, name='deletar_genero'),

    # URLs para o modelo Editora
    path('editoras/', lista_editoras, name='lista_editoras'),
    path('editora/<int:pk>/', detalhes_editora, name='detalhes_editora'),
    path('editora/nova/', nova_editora, name='nova_editora'),
    path('editora/editar/<int:pk>/', editar_editora, name='editar_editora'),
    path('editora/deletar/<int:pk>/', deletar_editora, name='deletar_editora'),

    # URLs para o modelo Autor
    path('autores/', lista_autores, name='lista_autores'),
    path('autor/<int:pk>/', detalhes_autor, name='detalhes_autor'),
    path('autor/novo/', novo_autor, name='novo_autor'),
    path('autor/editar/<int:pk>/', editar_autor, name='editar_autor'),
    path('autor/deletar/<int:pk>/', deletar_autor, name='deletar_autor'),

    # URLs para o modelo Livro
    path('livros/', lista_livros, name='lista_livros'),
    path('livro/<int:pk>/', detalhes_livro, name='detalhes_livro'),
    path('livro/novo/', novo_livro, name='novo_livro'),
    path('livro/editar/<int:pk>/', editar_livro, name='editar_livro'),
    path('livro/deletar/<int:pk>/', deletar_livro, name='deletar_livro'),
    path('livro/livros-recentes/', livros_recentes, name='livros_recentes'),
    path('livro/<int:pk>/gerar_pdf/', gerar_pdf_livro, name='gerar_pdf_livro'),

    # URLs para o modelo Exemplar
    path('exemplares/', lista_exemplares, name='lista_exemplares'),
    path('exemplar/<int:pk>/', detalhes_exemplar, name='detalhes_exemplar'),
    path('exemplar/novo/', novo_exemplar, name='novo_exemplar'),
    path('exemplar/editar/<int:pk>/', editar_exemplar, name='editar_exemplar'),
    path('exemplar/deletar/<int:pk>/', deletar_exemplar, name='deletar_exemplar'),

    # URLs para o modelo Funcionario
    path('funcionarios/', lista_funcionarios, name='lista_funcionarios'),
    path('funcionario/<int:pk>/', detalhes_funcionario, name='detalhes_funcionario'),
    path('funcionario/novo/', novo_funcionario, name='novo_funcionario'),
    path('funcionario/editar/<int:pk>/', editar_funcionario, name='editar_funcionario'),
    path('funcionario/deletar/<int:pk>/', deletar_funcionario, name='deletar_funcionario'),

    # URLs para o modelo Usuario
    path('usuarios/', lista_usuarios, name='lista_usuarios'),
    path('usuario/<int:pk>/', detalhes_usuario, name='detalhes_usuario'),
    path('usuario/novo/', novo_usuario, name='novo_usuario'),
    path('usuario/editar/<int:pk>/', editar_usuario, name='editar_usuario'),
    path('usuario/deletar/<int:pk>/', deletar_usuario, name='deletar_usuario'),

    # URLs para o modelo Emprestimo
    path('emprestimos/', lista_emprestimos, name='lista_emprestimos'),
    path('emprestimo/<int:pk>/', detalhes_emprestimo, name='detalhes_emprestimo'),
    path('emprestimo/novo/', novo_emprestimo, name='novo_emprestimo'),
    path('emprestimo/editar/<int:pk>/', editar_emprestimo, name='editar_emprestimo'),
    path('emprestimo/deletar/<int:pk>/', deletar_emprestimo, name='deletar_emprestimo'),

    # URLs para o modelo Multa
    path('multas/', lista_multas, name='lista_multas'),
    path('multa/<int:pk>/', detalhes_multa, name='detalhes_multa'),
    path('multa/nova/', nova_multa, name='nova_multa'),
    path('multa/editar/<int:pk>/', editar_multa, name='editar_multa'),
    path('multa/deletar/<int:pk>/', deletar_multa, name='deletar_multa'),

    # URLs para o modelo Comentario
    path('comentarios/', lista_comentarios, name='lista_comentarios'),
    path('comentario/<int:pk>/', detalhes_comentario, name='detalhes_comentario'),
    path('comentario/novo/', novo_comentario, name='novo_comentario'),
    path('comentario/editar/<int:pk>/', editar_comentario, name='editar_comentario'),
    path('comentario/deletar/<int:pk>/', deletar_comentario, name='deletar_comentario'),

    # URLs para o modelo Avaliacao
    path('avaliacoes/', lista_avaliacoes, name='lista_avaliacoes'),
    path('avaliacao/<int:pk>/', detalhes_avaliacao, name='detalhes_avaliacao'),
    path('avaliacao/nova/', nova_avaliacao, name='nova_avaliacao'),
    path('avaliacao/editar/<int:pk>/', editar_avaliacao, name='editar_avaliacao'),
    path('avaliacao/deletar/<int:pk>/', deletar_avaliacao, name='deletar_avaliacao'),

    # URLs para o modelo FuncLivro
    path('funclivros/', lista_func_livros, name='lista_func_livros'),
    path('funclivro/<int:pk>/', detalhes_func_livro, name='detalhes_func_livro'),
    path('funclivro/novo/', novo_func_livro, name='novo_func_livro'),
    path('funclivro/editar/<int:pk>/', editar_func_livro, name='editar_func_livro'),
    path('funclivro/deletar/<int:pk>/', deletar_func_livro, name='deletar_func_livro'),

    # URLs para o modelo Reserva
    path('reservas/', lista_reservas, name='lista_reservas'),
    path('reserva/<int:pk>/', detalhes_reserva, name='detalhes_reserva'),
    path('reserva/nova/', nova_reserva, name='nova_reserva'),
    path('reserva/editar/<int:pk>/', editar_reserva, name='editar_reserva'),
    path('reserva/deletar/<int:pk>/', deletar_reserva, name='deletar_reserva'),

    # URLs para o modelo Log
    path('logs/', lista_logs, name='lista_logs'),
    path('log/<int:pk>/', detalhes_log, name='detalhes_log'),
    path('log/novo/', novo_log, name='novo_log'),
    path('log/editar/<int:pk>/', editar_log, name='editar_log'),
    path('log/deletar/<int:pk>/', deletar_log, name='deletar_log'),

    # As URLs para os outros modelos continuam aqui...
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
