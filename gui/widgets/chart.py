#!/usr/bin/env python3

import tkinter as tk

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.ticker import FixedFormatter, FixedLocator

class Chart(tk.Frame):
    def __init__(self, parent, x_data=None, y_data=None, view_size=20, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.x_data = list(x_data) if x_data is not None else []
        self.y_data = y_data if y_data is not None else {}
        self.x_indices = list(range(len(self.x_data)))
        self.view_size = view_size

        self.fig = Figure(figsize=(5, 2), dpi=100)
        self.ax = self.fig.add_subplot(111)

        self.ax.set_ylim(0, 12)
        self.ax.set_yticks(range(13))
        self.ax.grid(True, linestyle='--', alpha=0.5)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self, orient=tk.HORIZONTAL, command=self._on_scroll)
        self.scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        if self.x_data:
            self.update_data(self.x_data, self.y_data)

    def update_data(self, new_x, new_y):
        self.x_data = list(new_x)
        self.y_data = new_y
        max_len = max([len(v) for v in self.y_data.values()]) if (isinstance(self.y_data, dict) and len(self.y_data) > 0) else 0
        self.x_indices = list(range(max_len))
        
        self.ax.clear()
        self.ax.set_ylim(0, 12)
        self.ax.invert_yaxis()
        self.ax.set_yticks(range(13))
        self.ax.grid(True, linestyle='--', alpha=0.3)

        if isinstance(self.y_data, dict):
            for name, values in self.y_data.items():
                current_x = list(range(len(values)))
                
                line, = self.ax.plot(current_x, values, marker='o', markersize=3, label=str(name), linewidth=1.5, zorder=2)

                current_color = line.get_color()
                def plot_medal(place, medal_color, size):
                    m_x = [current_x[i] for i, v in enumerate(values) if v is not None and int(v) == place]
                    if m_x:
                        self.ax.scatter(m_x, [place] * len(m_x),
                                        color=medal_color, s=size, zorder=3,
                                        edgecolors=current_color, linewidths=1)
                
            
                # Inny kolor dla pierwszego miejsca
                gold_x = [self.x_indices[i] for i, v in enumerate(values) if v is not None and int(v) == 1]
                gold_y = [1] * len(gold_x)
                if gold_x:
                    self.ax.scatter(gold_x, gold_y, color='gold', s=50, zorder=3, edgecolors='darkgoldenrod', linewidths=1)

                # Drugie miejsce
                silver_x = [self.x_indices[i] for i, v in enumerate(values) if v is not None and int(v) == 2]
                silver_y = [2] * len(silver_x)
                if silver_x:
                    self.ax.scatter(silver_x, silver_y, color='silver', s=50, zorder=3, edgecolors='dimgray', linewidths=0.5)

                # I trzecie
                bronze_x = [self.x_indices[i] for i, v in enumerate(values) if v is not None and int(v) == 3]
                bronze_y = [3] * len(bronze_x)
                if bronze_x:
                    self.ax.scatter(bronze_x, bronze_y, color='#CD7F32', s=50, zorder=3)

            if self.y_data:
                self.ax.legend(loc='lower left', fontsize='small', ncol=2 if len(self.y_data) >5 else 1)

        self.update_view()

    def _set_x_limits(self, start_idx):
        if not self.x_data: return
        end_idx = start_idx + self.view_size
        self.ax.set_xlim(start_idx - 0.5, end_idx - 0.5)

        visible_indices = list(range(start_idx, min(end_idx, len(self.x_data))))
        if visible_indices:
            self.ax.xaxis.set_major_locator(FixedLocator(visible_indices))
            self.ax.xaxis.set_major_formatter(FixedFormatter([str(self.x_data[i]) for i in visible_indices]))

        self.ax.tick_params(axis='x', labelrotation=90, labelsize=8)
        self.fig.tight_layout()
        self.canvas.draw_idle()

    def _on_scroll(self, *args):
        total = len(self.x_indices)
        if total <= self.view_size: return
        if args[0] == 'moveto': pos = float(args[1])
        else:
            curr = self.scrollbar.get()[0]
            pos = max(0, min(1.0, curr + (0.05 if args[1] == '1' else -0.05)))
        start_idx = int(pos * (total - self.view_size))
        self.scrollbar.set(start_idx/total, (start_idx + self.view_size)/total)
        self._set_x_limits(start_idx)

    def update_view(self):
        total = len(self.x_indices)
        if total <= self.view_size:
            self.ax.set_xlim(-0.5, self.view_size - 0.5)
            self.scrollbar.set(0.0, 1.0)
            self._set_x_limits(0)
        else:
            start_idx = total - self.view_size
            self._set_x_limits(start_idx)
            self.scrollbar.set(start_idx / total, 1.0)

        if hasattr(self, 'canvas'):
            self.canvas.draw()