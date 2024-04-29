import flet as ft
 
 
def main(page: ft.Page):
    page.bgcolor = ft.colors.BLACK
    page.title = "Habitos App"
    page.padding = ft.padding.all(30)
 
    habits_list =[
        {'title': 'Estudar Python', 'done': False},
        {'title': 'Praticar violão', 'done': False},
        {'title': 'Jogar Mário', 'done': False}
    ]
 
    def delete_habit(e, habit_title):
        habit = next ((hl for hl in habits_list if hl['title'] == habit_title), None)
        if habit:
            habits_list.remove(habit)
            refresh_habits_ui()
 
    def edit_habit(e, habit_title):
        # Encontra o hábito que está sendo editado
        habit = next ((hl for hl in habits_list if hl['title'] == habit_title), None)
        if habit is not None:
            # Substituir o checkbox por um Textfield
            index = habits_list.index(habit)
            habits.content.controls[index] = ft.Row(
                controls =[
                    ft.TextField(
                        value=habit['title'],
                        on_submit = lambda e, hl=habit: update_habit_title(e, hl),
                        autofocus = True,
                    )
                ]
            )
            habits.update()
   
    def update_habit_title(e, habit):
        habit['title'] = e.control.value
        refresh_habits_ui()
 
    def refresh_habits_ui():
        habits.content.controls = [
            ft.Row(
                controls = [
                    ft.Checkbox(
                        label = hl['title'],
                        value = hl['done'],
                        on_change = change
                    ),
                    ft.IconButton(
                        icon = ft.icons.EDIT,
                        icon_color = ft.colors.BLACK,
                        on_click = lambda e, hl=hl: edit_habit(e, hl['title'])
                    ),
                    ft.IconButton(
                        icon=ft.icons.DELETE,
                        icon_color=ft.colors.BLACK,
                        on_click=lambda e, hl=hl['title']: delete_habit(e, hl)
                    )
                ]
            ) for hl in habits_list
        ]
        habits.update()
 
    def change(e = None):
        if e:
            for hl in habits_list:
                if hl['title'] == e.control.label:
                    hl['done'] = e.control.value
       
        done = list(filter(lambda x: x['done'], habits_list))
        total = len(done) / len(habits_list)
        progress_bar.value = f'{total:.2f}'
        progress_text.value = f'{total: .0%}'
        progress_bar.update()
        progress_text.update()
 
    def add_habit(e):
        habits_list.append({'title': e.control.value, 'done':False})
        habits.content.controls = [
            ft.Row(
                controls = [
                    ft.Checkbox(
                        label = hl['title'],
                        value = hl['done'],
                        on_change = change
                    ),
                    ft.IconButton(
                        icon = ft.icons.EDIT,
                        icon_color = ft.colors.BLACK,
                        on_click = lambda e, hl=hl: edit_habit(e, hl['title'])
                    ),
                    ft.IconButton(
                        icon=ft.icons.DELETE,
                        icon_color=ft.colors.BLACK,
                        on_click=lambda e, hl=hl['title']: delete_habit(e, hl)
                    )
               
                ]
            )for hl in habits_list
        ]
        habits.update()
        e.control.value = ''
        e.control.update()
        change()
 
   
    layout = ft.Column(
        expand = True,
        controls=[
            ft.Text(value="Que bom ter você aqui", size=30, color=ft.colors.WHITE),
            ft.Text(value="Como estão seus hábitos hoje?", size=20, color=ft.colors.GREY),
 
            ft.Container(
                padding = ft.padding.all(30),
                bgcolor = ft.colors.INDIGO,
                border_radius = ft.border_radius.all(20),
                margin= ft.margin.symmetric(vertical=30),
                content = ft.Column(
                    controls =[
                        ft.Text(value='Sua evolução hoje', size=20, color=ft.colors.WHITE),
                        progress_text := ft.Text(value='0%', size=50, color=ft.colors.WHITE),
                        progress_bar := ft.ProgressBar(
                            value=0,
                            color=ft.colors.INDIGO_900,
                            bgcolor=ft.colors.INDIGO_100,
                            height=20,
                        ),
                    ],
                    horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                ),
            ),
 
            ft.Text(value='Hábitos de hoje', size=20, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
            ft.Text(value='Marcar suas tarefas como concluído te motiva a continuar focado', size=16, color=ft.colors.WHITE),
 
            habits := ft.Container(
                expand = True,
                padding = ft.padding.all(20),
                bgcolor = ft.colors.BROWN_50,
                border_radius = ft.border_radius.all(20),
                margin = ft.margin.symmetric(vertical=20),
                content= ft.Column(
                    expand = True,
                    scroll = ft.ScrollMode.AUTO,
                    spacing = 20,
                    controls =[
                        ft.Row(
                            controls=[
                                ft.Checkbox(
                                label=hl['title'],
                                value=hl['done'],
                                on_change=change
                                ),
                                ft.IconButton(
                                    icon=ft.icons.EDIT,
                                    icon_color=ft.colors.BLACK,
                                    on_click = lambda e, hl=hl: edit_habit (e, hl['title'])
                                ),
                                ft.IconButton(
                                    icon=ft.icons.DELETE,
                                    icon_color=ft.colors.BLACK,
                                    on_click=lambda e, hl=hl['title']: delete_habit(e, hl)
                                )
                            ]
                        )for hl in habits_list
                    ]
                   
                ),
 
            ),
 
            ft.Text(value="Adicionar novo hábito", size=20, color=ft.colors.WHITE),
            ft.TextField(hint_text='Escreva um hábito...', border=ft.InputBorder.UNDERLINE,
                         border_color=ft.colors.WHITE,
                         bgcolor=ft.colors.GREY_50,
                         on_submit=add_habit)
 
        ]
    )
 
    page.add(layout)
 
    page.update()
 
 
ft.app(main)
 