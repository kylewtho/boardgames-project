{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Quantum tic-tac-toe.py",
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    },
    "widgets": {
      "application/vnd.jupyter.widget-state+json": {
        "14e04589d4754c078287878fcabaa476": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "ButtonModel",
          "model_module_version": "1.5.0",
          "state": {
            "_view_name": "ButtonView",
            "style": "IPY_MODEL_104ba15919954ad1a32a6bcfab251ca2",
            "_dom_classes": [],
            "description": "Measure",
            "_model_name": "ButtonModel",
            "button_style": "",
            "_view_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "tooltip": "",
            "_view_count": null,
            "disabled": false,
            "_view_module_version": "1.5.0",
            "layout": "IPY_MODEL_2deff77114ad4729b29fe60abe7cc731",
            "_model_module": "@jupyter-widgets/controls",
            "icon": ""
          }
        },
        "104ba15919954ad1a32a6bcfab251ca2": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "ButtonStyleModel",
          "model_module_version": "1.5.0",
          "state": {
            "_view_name": "StyleView",
            "_model_name": "ButtonStyleModel",
            "_view_module": "@jupyter-widgets/base",
            "_model_module_version": "1.5.0",
            "_view_count": null,
            "button_color": null,
            "font_weight": "",
            "_view_module_version": "1.2.0",
            "_model_module": "@jupyter-widgets/controls"
          }
        },
        "2deff77114ad4729b29fe60abe7cc731": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_view_name": "LayoutView",
            "grid_template_rows": null,
            "right": null,
            "justify_content": null,
            "_view_module": "@jupyter-widgets/base",
            "overflow": null,
            "_model_module_version": "1.2.0",
            "_view_count": null,
            "flex_flow": null,
            "width": "86px",
            "min_width": null,
            "border": null,
            "align_items": null,
            "bottom": null,
            "_model_module": "@jupyter-widgets/base",
            "top": null,
            "grid_column": null,
            "overflow_y": null,
            "overflow_x": null,
            "grid_auto_flow": null,
            "grid_area": null,
            "grid_template_columns": null,
            "flex": null,
            "_model_name": "LayoutModel",
            "justify_items": null,
            "grid_row": null,
            "max_height": null,
            "align_content": null,
            "visibility": null,
            "align_self": null,
            "height": "30px",
            "min_height": null,
            "padding": null,
            "grid_auto_rows": null,
            "grid_gap": null,
            "max_width": null,
            "order": null,
            "_view_module_version": "1.2.0",
            "grid_template_areas": null,
            "object_position": null,
            "object_fit": null,
            "grid_auto_columns": null,
            "margin": null,
            "display": null,
            "left": null
          }
        },
        "dc721c091aad489582e7d2315185a908": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "ButtonModel",
          "model_module_version": "1.5.0",
          "state": {
            "_view_name": "ButtonView",
            "style": "IPY_MODEL_599c7e30166d457ba99579c8ce841959",
            "_dom_classes": [],
            "description": "Not",
            "_model_name": "ButtonModel",
            "button_style": "",
            "_view_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "tooltip": "",
            "_view_count": null,
            "disabled": false,
            "_view_module_version": "1.5.0",
            "layout": "IPY_MODEL_77d5615fe95549dc9094816b826494d0",
            "_model_module": "@jupyter-widgets/controls",
            "icon": ""
          }
        },
        "599c7e30166d457ba99579c8ce841959": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "ButtonStyleModel",
          "model_module_version": "1.5.0",
          "state": {
            "_view_name": "StyleView",
            "_model_name": "ButtonStyleModel",
            "_view_module": "@jupyter-widgets/base",
            "_model_module_version": "1.5.0",
            "_view_count": null,
            "button_color": null,
            "font_weight": "",
            "_view_module_version": "1.2.0",
            "_model_module": "@jupyter-widgets/controls"
          }
        },
        "77d5615fe95549dc9094816b826494d0": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_view_name": "LayoutView",
            "grid_template_rows": null,
            "right": null,
            "justify_content": null,
            "_view_module": "@jupyter-widgets/base",
            "overflow": null,
            "_model_module_version": "1.2.0",
            "_view_count": null,
            "flex_flow": null,
            "width": "86px",
            "min_width": null,
            "border": null,
            "align_items": null,
            "bottom": null,
            "_model_module": "@jupyter-widgets/base",
            "top": null,
            "grid_column": null,
            "overflow_y": null,
            "overflow_x": null,
            "grid_auto_flow": null,
            "grid_area": null,
            "grid_template_columns": null,
            "flex": null,
            "_model_name": "LayoutModel",
            "justify_items": null,
            "grid_row": null,
            "max_height": null,
            "align_content": null,
            "visibility": null,
            "align_self": null,
            "height": "30px",
            "min_height": null,
            "padding": null,
            "grid_auto_rows": null,
            "grid_gap": null,
            "max_width": null,
            "order": null,
            "_view_module_version": "1.2.0",
            "grid_template_areas": null,
            "object_position": null,
            "object_fit": null,
            "grid_auto_columns": null,
            "margin": null,
            "display": null,
            "left": null
          }
        },
        "d8c49f3989c94b028603f948768b219f": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "ButtonModel",
          "model_module_version": "1.5.0",
          "state": {
            "_view_name": "ButtonView",
            "style": "IPY_MODEL_b52160942f20420f8e9be0471b639b0a",
            "_dom_classes": [],
            "description": "O",
            "_model_name": "ButtonModel",
            "button_style": "",
            "_view_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "tooltip": "",
            "_view_count": null,
            "disabled": false,
            "_view_module_version": "1.5.0",
            "layout": "IPY_MODEL_b29d7bbeb4ec4cbe8b08c7d42af66b1a",
            "_model_module": "@jupyter-widgets/controls",
            "icon": ""
          }
        },
        "b52160942f20420f8e9be0471b639b0a": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "ButtonStyleModel",
          "model_module_version": "1.5.0",
          "state": {
            "_view_name": "StyleView",
            "_model_name": "ButtonStyleModel",
            "_view_module": "@jupyter-widgets/base",
            "_model_module_version": "1.5.0",
            "_view_count": null,
            "button_color": null,
            "font_weight": "",
            "_view_module_version": "1.2.0",
            "_model_module": "@jupyter-widgets/controls"
          }
        },
        "b29d7bbeb4ec4cbe8b08c7d42af66b1a": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_view_name": "LayoutView",
            "grid_template_rows": null,
            "right": null,
            "justify_content": null,
            "_view_module": "@jupyter-widgets/base",
            "overflow": null,
            "_model_module_version": "1.2.0",
            "_view_count": null,
            "flex_flow": null,
            "width": "86px",
            "min_width": null,
            "border": null,
            "align_items": null,
            "bottom": null,
            "_model_module": "@jupyter-widgets/base",
            "top": null,
            "grid_column": null,
            "overflow_y": null,
            "overflow_x": null,
            "grid_auto_flow": null,
            "grid_area": null,
            "grid_template_columns": null,
            "flex": null,
            "_model_name": "LayoutModel",
            "justify_items": null,
            "grid_row": null,
            "max_height": null,
            "align_content": null,
            "visibility": null,
            "align_self": null,
            "height": "30px",
            "min_height": null,
            "padding": null,
            "grid_auto_rows": null,
            "grid_gap": null,
            "max_width": null,
            "order": null,
            "_view_module_version": "1.2.0",
            "grid_template_areas": null,
            "object_position": null,
            "object_fit": null,
            "grid_auto_columns": null,
            "margin": null,
            "display": null,
            "left": null
          }
        },
        "299eb30a65fd4eb0ac4c339503a2eba5": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "ButtonModel",
          "model_module_version": "1.5.0",
          "state": {
            "_view_name": "ButtonView",
            "style": "IPY_MODEL_03332e3e638d4f8ab57b8971e4c6813b",
            "_dom_classes": [],
            "description": "X",
            "_model_name": "ButtonModel",
            "button_style": "",
            "_view_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "tooltip": "",
            "_view_count": null,
            "disabled": false,
            "_view_module_version": "1.5.0",
            "layout": "IPY_MODEL_cd2219bdadec401582211c24f4bae09f",
            "_model_module": "@jupyter-widgets/controls",
            "icon": ""
          }
        },
        "03332e3e638d4f8ab57b8971e4c6813b": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "ButtonStyleModel",
          "model_module_version": "1.5.0",
          "state": {
            "_view_name": "StyleView",
            "_model_name": "ButtonStyleModel",
            "_view_module": "@jupyter-widgets/base",
            "_model_module_version": "1.5.0",
            "_view_count": null,
            "button_color": null,
            "font_weight": "",
            "_view_module_version": "1.2.0",
            "_model_module": "@jupyter-widgets/controls"
          }
        },
        "cd2219bdadec401582211c24f4bae09f": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_view_name": "LayoutView",
            "grid_template_rows": null,
            "right": null,
            "justify_content": null,
            "_view_module": "@jupyter-widgets/base",
            "overflow": null,
            "_model_module_version": "1.2.0",
            "_view_count": null,
            "flex_flow": null,
            "width": "86px",
            "min_width": null,
            "border": null,
            "align_items": null,
            "bottom": null,
            "_model_module": "@jupyter-widgets/base",
            "top": null,
            "grid_column": null,
            "overflow_y": null,
            "overflow_x": null,
            "grid_auto_flow": null,
            "grid_area": null,
            "grid_template_columns": null,
            "flex": null,
            "_model_name": "LayoutModel",
            "justify_items": null,
            "grid_row": null,
            "max_height": null,
            "align_content": null,
            "visibility": null,
            "align_self": null,
            "height": "30px",
            "min_height": null,
            "padding": null,
            "grid_auto_rows": null,
            "grid_gap": null,
            "max_width": null,
            "order": null,
            "_view_module_version": "1.2.0",
            "grid_template_areas": null,
            "object_position": null,
            "object_fit": null,
            "grid_auto_columns": null,
            "margin": null,
            "display": null,
            "left": null
          }
        },
        "459a59fe7aec4bd398065c10f0163cdb": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "ButtonModel",
          "model_module_version": "1.5.0",
          "state": {
            "_view_name": "ButtonView",
            "style": "IPY_MODEL_18c3d0b9515f49c6b4717aa38f025c4e",
            "_dom_classes": [],
            "description": "SWAP",
            "_model_name": "ButtonModel",
            "button_style": "",
            "_view_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "tooltip": "",
            "_view_count": null,
            "disabled": false,
            "_view_module_version": "1.5.0",
            "layout": "IPY_MODEL_52882fa4ee11469f982cc0a56b525d0f",
            "_model_module": "@jupyter-widgets/controls",
            "icon": ""
          }
        },
        "18c3d0b9515f49c6b4717aa38f025c4e": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "ButtonStyleModel",
          "model_module_version": "1.5.0",
          "state": {
            "_view_name": "StyleView",
            "_model_name": "ButtonStyleModel",
            "_view_module": "@jupyter-widgets/base",
            "_model_module_version": "1.5.0",
            "_view_count": null,
            "button_color": null,
            "font_weight": "",
            "_view_module_version": "1.2.0",
            "_model_module": "@jupyter-widgets/controls"
          }
        },
        "52882fa4ee11469f982cc0a56b525d0f": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_view_name": "LayoutView",
            "grid_template_rows": null,
            "right": null,
            "justify_content": null,
            "_view_module": "@jupyter-widgets/base",
            "overflow": null,
            "_model_module_version": "1.2.0",
            "_view_count": null,
            "flex_flow": null,
            "width": "86px",
            "min_width": null,
            "border": null,
            "align_items": null,
            "bottom": null,
            "_model_module": "@jupyter-widgets/base",
            "top": null,
            "grid_column": null,
            "overflow_y": null,
            "overflow_x": null,
            "grid_auto_flow": null,
            "grid_area": null,
            "grid_template_columns": null,
            "flex": null,
            "_model_name": "LayoutModel",
            "justify_items": null,
            "grid_row": null,
            "max_height": null,
            "align_content": null,
            "visibility": null,
            "align_self": null,
            "height": "30px",
            "min_height": null,
            "padding": null,
            "grid_auto_rows": null,
            "grid_gap": null,
            "max_width": null,
            "order": null,
            "_view_module_version": "1.2.0",
            "grid_template_areas": null,
            "object_position": null,
            "object_fit": null,
            "grid_auto_columns": null,
            "margin": null,
            "display": null,
            "left": null
          }
        },
        "2be9e144ab5045abbbeb875b0f886fcb": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "ButtonModel",
          "model_module_version": "1.5.0",
          "state": {
            "_view_name": "ButtonView",
            "style": "IPY_MODEL_e924fe6b79fd4650b8cd089c157d113f",
            "_dom_classes": [],
            "description": "0",
            "_model_name": "ButtonModel",
            "button_style": "",
            "_view_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "tooltip": "",
            "_view_count": null,
            "disabled": false,
            "_view_module_version": "1.5.0",
            "layout": "IPY_MODEL_651fa03154bf48368bba9d8725d26927",
            "_model_module": "@jupyter-widgets/controls",
            "icon": ""
          }
        },
        "e924fe6b79fd4650b8cd089c157d113f": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "ButtonStyleModel",
          "model_module_version": "1.5.0",
          "state": {
            "_view_name": "StyleView",
            "_model_name": "ButtonStyleModel",
            "_view_module": "@jupyter-widgets/base",
            "_model_module_version": "1.5.0",
            "_view_count": null,
            "button_color": null,
            "font_weight": "",
            "_view_module_version": "1.2.0",
            "_model_module": "@jupyter-widgets/controls"
          }
        },
        "651fa03154bf48368bba9d8725d26927": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_view_name": "LayoutView",
            "grid_template_rows": null,
            "right": null,
            "justify_content": null,
            "_view_module": "@jupyter-widgets/base",
            "overflow": null,
            "_model_module_version": "1.2.0",
            "_view_count": null,
            "flex_flow": null,
            "width": null,
            "min_width": null,
            "border": null,
            "align_items": null,
            "bottom": null,
            "_model_module": "@jupyter-widgets/base",
            "top": null,
            "grid_column": null,
            "overflow_y": null,
            "overflow_x": null,
            "grid_auto_flow": null,
            "grid_area": null,
            "grid_template_columns": null,
            "flex": null,
            "_model_name": "LayoutModel",
            "justify_items": null,
            "grid_row": null,
            "max_height": null,
            "align_content": null,
            "visibility": null,
            "align_self": null,
            "height": null,
            "min_height": null,
            "padding": null,
            "grid_auto_rows": null,
            "grid_gap": null,
            "max_width": null,
            "order": null,
            "_view_module_version": "1.2.0",
            "grid_template_areas": null,
            "object_position": null,
            "object_fit": null,
            "grid_auto_columns": null,
            "margin": null,
            "display": null,
            "left": null
          }
        },
        "90c0deae0349447d9c2d85a1e516efe6": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "ButtonModel",
          "model_module_version": "1.5.0",
          "state": {
            "_view_name": "ButtonView",
            "style": "IPY_MODEL_fcb38b2d8acb43288390d9794cb2e8f6",
            "_dom_classes": [],
            "description": "1",
            "_model_name": "ButtonModel",
            "button_style": "",
            "_view_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "tooltip": "",
            "_view_count": null,
            "disabled": false,
            "_view_module_version": "1.5.0",
            "layout": "IPY_MODEL_d42a99b06ebd474a9ec829851599b240",
            "_model_module": "@jupyter-widgets/controls",
            "icon": ""
          }
        },
        "fcb38b2d8acb43288390d9794cb2e8f6": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "ButtonStyleModel",
          "model_module_version": "1.5.0",
          "state": {
            "_view_name": "StyleView",
            "_model_name": "ButtonStyleModel",
            "_view_module": "@jupyter-widgets/base",
            "_model_module_version": "1.5.0",
            "_view_count": null,
            "button_color": null,
            "font_weight": "",
            "_view_module_version": "1.2.0",
            "_model_module": "@jupyter-widgets/controls"
          }
        },
        "d42a99b06ebd474a9ec829851599b240": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_view_name": "LayoutView",
            "grid_template_rows": null,
            "right": null,
            "justify_content": null,
            "_view_module": "@jupyter-widgets/base",
            "overflow": null,
            "_model_module_version": "1.2.0",
            "_view_count": null,
            "flex_flow": null,
            "width": null,
            "min_width": null,
            "border": null,
            "align_items": null,
            "bottom": null,
            "_model_module": "@jupyter-widgets/base",
            "top": null,
            "grid_column": null,
            "overflow_y": null,
            "overflow_x": null,
            "grid_auto_flow": null,
            "grid_area": null,
            "grid_template_columns": null,
            "flex": null,
            "_model_name": "LayoutModel",
            "justify_items": null,
            "grid_row": null,
            "max_height": null,
            "align_content": null,
            "visibility": null,
            "align_self": null,
            "height": null,
            "min_height": null,
            "padding": null,
            "grid_auto_rows": null,
            "grid_gap": null,
            "max_width": null,
            "order": null,
            "_view_module_version": "1.2.0",
            "grid_template_areas": null,
            "object_position": null,
            "object_fit": null,
            "grid_auto_columns": null,
            "margin": null,
            "display": null,
            "left": null
          }
        },
        "bb57b7c0d6554231a28c9ee5febb1b87": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "ButtonModel",
          "model_module_version": "1.5.0",
          "state": {
            "_view_name": "ButtonView",
            "style": "IPY_MODEL_bf7d9dddce4343baa0401a4afebe8c2c",
            "_dom_classes": [],
            "description": "2",
            "_model_name": "ButtonModel",
            "button_style": "",
            "_view_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "tooltip": "",
            "_view_count": null,
            "disabled": false,
            "_view_module_version": "1.5.0",
            "layout": "IPY_MODEL_a87b6f5972d84cc0ad039cb8cef8b94a",
            "_model_module": "@jupyter-widgets/controls",
            "icon": ""
          }
        },
        "bf7d9dddce4343baa0401a4afebe8c2c": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "ButtonStyleModel",
          "model_module_version": "1.5.0",
          "state": {
            "_view_name": "StyleView",
            "_model_name": "ButtonStyleModel",
            "_view_module": "@jupyter-widgets/base",
            "_model_module_version": "1.5.0",
            "_view_count": null,
            "button_color": null,
            "font_weight": "",
            "_view_module_version": "1.2.0",
            "_model_module": "@jupyter-widgets/controls"
          }
        },
        "a87b6f5972d84cc0ad039cb8cef8b94a": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_view_name": "LayoutView",
            "grid_template_rows": null,
            "right": null,
            "justify_content": null,
            "_view_module": "@jupyter-widgets/base",
            "overflow": null,
            "_model_module_version": "1.2.0",
            "_view_count": null,
            "flex_flow": null,
            "width": null,
            "min_width": null,
            "border": null,
            "align_items": null,
            "bottom": null,
            "_model_module": "@jupyter-widgets/base",
            "top": null,
            "grid_column": null,
            "overflow_y": null,
            "overflow_x": null,
            "grid_auto_flow": null,
            "grid_area": null,
            "grid_template_columns": null,
            "flex": null,
            "_model_name": "LayoutModel",
            "justify_items": null,
            "grid_row": null,
            "max_height": null,
            "align_content": null,
            "visibility": null,
            "align_self": null,
            "height": null,
            "min_height": null,
            "padding": null,
            "grid_auto_rows": null,
            "grid_gap": null,
            "max_width": null,
            "order": null,
            "_view_module_version": "1.2.0",
            "grid_template_areas": null,
            "object_position": null,
            "object_fit": null,
            "grid_auto_columns": null,
            "margin": null,
            "display": null,
            "left": null
          }
        },
        "81fcb49ab44d41e88b2e179c601f0d59": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "ButtonModel",
          "model_module_version": "1.5.0",
          "state": {
            "_view_name": "ButtonView",
            "style": "IPY_MODEL_fb8ab179a8d043e9bae92f869f1a9f20",
            "_dom_classes": [],
            "description": "3",
            "_model_name": "ButtonModel",
            "button_style": "",
            "_view_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "tooltip": "",
            "_view_count": null,
            "disabled": false,
            "_view_module_version": "1.5.0",
            "layout": "IPY_MODEL_05d87db07b5c4999af986b4d0486ad53",
            "_model_module": "@jupyter-widgets/controls",
            "icon": ""
          }
        },
        "fb8ab179a8d043e9bae92f869f1a9f20": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "ButtonStyleModel",
          "model_module_version": "1.5.0",
          "state": {
            "_view_name": "StyleView",
            "_model_name": "ButtonStyleModel",
            "_view_module": "@jupyter-widgets/base",
            "_model_module_version": "1.5.0",
            "_view_count": null,
            "button_color": null,
            "font_weight": "",
            "_view_module_version": "1.2.0",
            "_model_module": "@jupyter-widgets/controls"
          }
        },
        "05d87db07b5c4999af986b4d0486ad53": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_view_name": "LayoutView",
            "grid_template_rows": null,
            "right": null,
            "justify_content": null,
            "_view_module": "@jupyter-widgets/base",
            "overflow": null,
            "_model_module_version": "1.2.0",
            "_view_count": null,
            "flex_flow": null,
            "width": null,
            "min_width": null,
            "border": null,
            "align_items": null,
            "bottom": null,
            "_model_module": "@jupyter-widgets/base",
            "top": null,
            "grid_column": null,
            "overflow_y": null,
            "overflow_x": null,
            "grid_auto_flow": null,
            "grid_area": null,
            "grid_template_columns": null,
            "flex": null,
            "_model_name": "LayoutModel",
            "justify_items": null,
            "grid_row": null,
            "max_height": null,
            "align_content": null,
            "visibility": null,
            "align_self": null,
            "height": null,
            "min_height": null,
            "padding": null,
            "grid_auto_rows": null,
            "grid_gap": null,
            "max_width": null,
            "order": null,
            "_view_module_version": "1.2.0",
            "grid_template_areas": null,
            "object_position": null,
            "object_fit": null,
            "grid_auto_columns": null,
            "margin": null,
            "display": null,
            "left": null
          }
        },
        "f2b8e4dbab11422993b008639c9293ba": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "ButtonModel",
          "model_module_version": "1.5.0",
          "state": {
            "_view_name": "ButtonView",
            "style": "IPY_MODEL_12b20ca76ac9456bb63e9aa7b9579208",
            "_dom_classes": [],
            "description": "4",
            "_model_name": "ButtonModel",
            "button_style": "",
            "_view_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "tooltip": "",
            "_view_count": null,
            "disabled": false,
            "_view_module_version": "1.5.0",
            "layout": "IPY_MODEL_4f6db24019f64b76ae67efb2e3f47d99",
            "_model_module": "@jupyter-widgets/controls",
            "icon": ""
          }
        },
        "12b20ca76ac9456bb63e9aa7b9579208": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "ButtonStyleModel",
          "model_module_version": "1.5.0",
          "state": {
            "_view_name": "StyleView",
            "_model_name": "ButtonStyleModel",
            "_view_module": "@jupyter-widgets/base",
            "_model_module_version": "1.5.0",
            "_view_count": null,
            "button_color": null,
            "font_weight": "",
            "_view_module_version": "1.2.0",
            "_model_module": "@jupyter-widgets/controls"
          }
        },
        "4f6db24019f64b76ae67efb2e3f47d99": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_view_name": "LayoutView",
            "grid_template_rows": null,
            "right": null,
            "justify_content": null,
            "_view_module": "@jupyter-widgets/base",
            "overflow": null,
            "_model_module_version": "1.2.0",
            "_view_count": null,
            "flex_flow": null,
            "width": null,
            "min_width": null,
            "border": null,
            "align_items": null,
            "bottom": null,
            "_model_module": "@jupyter-widgets/base",
            "top": null,
            "grid_column": null,
            "overflow_y": null,
            "overflow_x": null,
            "grid_auto_flow": null,
            "grid_area": null,
            "grid_template_columns": null,
            "flex": null,
            "_model_name": "LayoutModel",
            "justify_items": null,
            "grid_row": null,
            "max_height": null,
            "align_content": null,
            "visibility": null,
            "align_self": null,
            "height": null,
            "min_height": null,
            "padding": null,
            "grid_auto_rows": null,
            "grid_gap": null,
            "max_width": null,
            "order": null,
            "_view_module_version": "1.2.0",
            "grid_template_areas": null,
            "object_position": null,
            "object_fit": null,
            "grid_auto_columns": null,
            "margin": null,
            "display": null,
            "left": null
          }
        },
        "7dbecb7a95b24a8c9a74f5dd2f1d4449": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "ButtonModel",
          "model_module_version": "1.5.0",
          "state": {
            "_view_name": "ButtonView",
            "style": "IPY_MODEL_dba1109aaa35429498c94be67d9530ba",
            "_dom_classes": [],
            "description": "5",
            "_model_name": "ButtonModel",
            "button_style": "",
            "_view_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "tooltip": "",
            "_view_count": null,
            "disabled": false,
            "_view_module_version": "1.5.0",
            "layout": "IPY_MODEL_fb32dda1c58a458eac7625c406058458",
            "_model_module": "@jupyter-widgets/controls",
            "icon": ""
          }
        },
        "dba1109aaa35429498c94be67d9530ba": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "ButtonStyleModel",
          "model_module_version": "1.5.0",
          "state": {
            "_view_name": "StyleView",
            "_model_name": "ButtonStyleModel",
            "_view_module": "@jupyter-widgets/base",
            "_model_module_version": "1.5.0",
            "_view_count": null,
            "button_color": null,
            "font_weight": "",
            "_view_module_version": "1.2.0",
            "_model_module": "@jupyter-widgets/controls"
          }
        },
        "fb32dda1c58a458eac7625c406058458": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_view_name": "LayoutView",
            "grid_template_rows": null,
            "right": null,
            "justify_content": null,
            "_view_module": "@jupyter-widgets/base",
            "overflow": null,
            "_model_module_version": "1.2.0",
            "_view_count": null,
            "flex_flow": null,
            "width": null,
            "min_width": null,
            "border": null,
            "align_items": null,
            "bottom": null,
            "_model_module": "@jupyter-widgets/base",
            "top": null,
            "grid_column": null,
            "overflow_y": null,
            "overflow_x": null,
            "grid_auto_flow": null,
            "grid_area": null,
            "grid_template_columns": null,
            "flex": null,
            "_model_name": "LayoutModel",
            "justify_items": null,
            "grid_row": null,
            "max_height": null,
            "align_content": null,
            "visibility": null,
            "align_self": null,
            "height": null,
            "min_height": null,
            "padding": null,
            "grid_auto_rows": null,
            "grid_gap": null,
            "max_width": null,
            "order": null,
            "_view_module_version": "1.2.0",
            "grid_template_areas": null,
            "object_position": null,
            "object_fit": null,
            "grid_auto_columns": null,
            "margin": null,
            "display": null,
            "left": null
          }
        },
        "72e04da17254451f8e375dec1dce2b76": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "ButtonModel",
          "model_module_version": "1.5.0",
          "state": {
            "_view_name": "ButtonView",
            "style": "IPY_MODEL_bb874be13d0042369b922748c9c594f2",
            "_dom_classes": [],
            "description": "6",
            "_model_name": "ButtonModel",
            "button_style": "",
            "_view_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "tooltip": "",
            "_view_count": null,
            "disabled": false,
            "_view_module_version": "1.5.0",
            "layout": "IPY_MODEL_c19d20deb2c84c3eabecf3952f5d9f7e",
            "_model_module": "@jupyter-widgets/controls",
            "icon": ""
          }
        },
        "bb874be13d0042369b922748c9c594f2": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "ButtonStyleModel",
          "model_module_version": "1.5.0",
          "state": {
            "_view_name": "StyleView",
            "_model_name": "ButtonStyleModel",
            "_view_module": "@jupyter-widgets/base",
            "_model_module_version": "1.5.0",
            "_view_count": null,
            "button_color": null,
            "font_weight": "",
            "_view_module_version": "1.2.0",
            "_model_module": "@jupyter-widgets/controls"
          }
        },
        "c19d20deb2c84c3eabecf3952f5d9f7e": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_view_name": "LayoutView",
            "grid_template_rows": null,
            "right": null,
            "justify_content": null,
            "_view_module": "@jupyter-widgets/base",
            "overflow": null,
            "_model_module_version": "1.2.0",
            "_view_count": null,
            "flex_flow": null,
            "width": null,
            "min_width": null,
            "border": null,
            "align_items": null,
            "bottom": null,
            "_model_module": "@jupyter-widgets/base",
            "top": null,
            "grid_column": null,
            "overflow_y": null,
            "overflow_x": null,
            "grid_auto_flow": null,
            "grid_area": null,
            "grid_template_columns": null,
            "flex": null,
            "_model_name": "LayoutModel",
            "justify_items": null,
            "grid_row": null,
            "max_height": null,
            "align_content": null,
            "visibility": null,
            "align_self": null,
            "height": null,
            "min_height": null,
            "padding": null,
            "grid_auto_rows": null,
            "grid_gap": null,
            "max_width": null,
            "order": null,
            "_view_module_version": "1.2.0",
            "grid_template_areas": null,
            "object_position": null,
            "object_fit": null,
            "grid_auto_columns": null,
            "margin": null,
            "display": null,
            "left": null
          }
        },
        "ff8b733f22bc43858aa44c005ec0e7ba": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "ButtonModel",
          "model_module_version": "1.5.0",
          "state": {
            "_view_name": "ButtonView",
            "style": "IPY_MODEL_8a70c0ca8aa64e8f93603a896921177a",
            "_dom_classes": [],
            "description": "7",
            "_model_name": "ButtonModel",
            "button_style": "",
            "_view_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "tooltip": "",
            "_view_count": null,
            "disabled": false,
            "_view_module_version": "1.5.0",
            "layout": "IPY_MODEL_892ada0e75604400921806951ab778fd",
            "_model_module": "@jupyter-widgets/controls",
            "icon": ""
          }
        },
        "8a70c0ca8aa64e8f93603a896921177a": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "ButtonStyleModel",
          "model_module_version": "1.5.0",
          "state": {
            "_view_name": "StyleView",
            "_model_name": "ButtonStyleModel",
            "_view_module": "@jupyter-widgets/base",
            "_model_module_version": "1.5.0",
            "_view_count": null,
            "button_color": null,
            "font_weight": "",
            "_view_module_version": "1.2.0",
            "_model_module": "@jupyter-widgets/controls"
          }
        },
        "892ada0e75604400921806951ab778fd": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_view_name": "LayoutView",
            "grid_template_rows": null,
            "right": null,
            "justify_content": null,
            "_view_module": "@jupyter-widgets/base",
            "overflow": null,
            "_model_module_version": "1.2.0",
            "_view_count": null,
            "flex_flow": null,
            "width": null,
            "min_width": null,
            "border": null,
            "align_items": null,
            "bottom": null,
            "_model_module": "@jupyter-widgets/base",
            "top": null,
            "grid_column": null,
            "overflow_y": null,
            "overflow_x": null,
            "grid_auto_flow": null,
            "grid_area": null,
            "grid_template_columns": null,
            "flex": null,
            "_model_name": "LayoutModel",
            "justify_items": null,
            "grid_row": null,
            "max_height": null,
            "align_content": null,
            "visibility": null,
            "align_self": null,
            "height": null,
            "min_height": null,
            "padding": null,
            "grid_auto_rows": null,
            "grid_gap": null,
            "max_width": null,
            "order": null,
            "_view_module_version": "1.2.0",
            "grid_template_areas": null,
            "object_position": null,
            "object_fit": null,
            "grid_auto_columns": null,
            "margin": null,
            "display": null,
            "left": null
          }
        },
        "1bce1417447d4d53885e8ba8ab3934c9": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "ButtonModel",
          "model_module_version": "1.5.0",
          "state": {
            "_view_name": "ButtonView",
            "style": "IPY_MODEL_491f3c68d5f548beaf8014bd225bfbf0",
            "_dom_classes": [],
            "description": "8",
            "_model_name": "ButtonModel",
            "button_style": "",
            "_view_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "tooltip": "",
            "_view_count": null,
            "disabled": false,
            "_view_module_version": "1.5.0",
            "layout": "IPY_MODEL_b2180747aea34645a595a23828fb2259",
            "_model_module": "@jupyter-widgets/controls",
            "icon": ""
          }
        },
        "491f3c68d5f548beaf8014bd225bfbf0": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "ButtonStyleModel",
          "model_module_version": "1.5.0",
          "state": {
            "_view_name": "StyleView",
            "_model_name": "ButtonStyleModel",
            "_view_module": "@jupyter-widgets/base",
            "_model_module_version": "1.5.0",
            "_view_count": null,
            "button_color": null,
            "font_weight": "",
            "_view_module_version": "1.2.0",
            "_model_module": "@jupyter-widgets/controls"
          }
        },
        "b2180747aea34645a595a23828fb2259": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_view_name": "LayoutView",
            "grid_template_rows": null,
            "right": null,
            "justify_content": null,
            "_view_module": "@jupyter-widgets/base",
            "overflow": null,
            "_model_module_version": "1.2.0",
            "_view_count": null,
            "flex_flow": null,
            "width": null,
            "min_width": null,
            "border": null,
            "align_items": null,
            "bottom": null,
            "_model_module": "@jupyter-widgets/base",
            "top": null,
            "grid_column": null,
            "overflow_y": null,
            "overflow_x": null,
            "grid_auto_flow": null,
            "grid_area": null,
            "grid_template_columns": null,
            "flex": null,
            "_model_name": "LayoutModel",
            "justify_items": null,
            "grid_row": null,
            "max_height": null,
            "align_content": null,
            "visibility": null,
            "align_self": null,
            "height": null,
            "min_height": null,
            "padding": null,
            "grid_auto_rows": null,
            "grid_gap": null,
            "max_width": null,
            "order": null,
            "_view_module_version": "1.2.0",
            "grid_template_areas": null,
            "object_position": null,
            "object_fit": null,
            "grid_auto_columns": null,
            "margin": null,
            "display": null,
            "left": null
          }
        }
      }
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/kylewtho/boardgames-project/blob/main/Quantum_tic_tac_toe_py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "DnbgsNM__Z01"
      },
      "source": [
        "Set up the game logic"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "B1RWWNCjPDvO",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "bf63a1a3-e7f0-41c5-b8d8-a1dc2d5fd085"
      },
      "source": [
        "!pip install qiskit --quiet\n",
        "!pip install pylatexenc --quiet\n",
        "\n",
        "from qiskit import *\n",
        "from qiskit.visualization import plot_histogram\n",
        "from google.colab import widgets\n",
        "from __future__ import print_function\n",
        "from ipywidgets import interact, interactive, fixed, interact_manual, Button, Layout\n",
        "import ipywidgets\n",
        "import pandas as pd\n",
        "import math\n",
        "import numpy as np\n",
        "import random\n",
        "from IPython.display import clear_output"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[K     |████████████████████████████████| 6.1 MB 6.1 MB/s \n",
            "\u001b[K     |████████████████████████████████| 17.9 MB 109 kB/s \n",
            "\u001b[K     |████████████████████████████████| 236 kB 41.6 MB/s \n",
            "\u001b[K     |████████████████████████████████| 207 kB 38.2 MB/s \n",
            "\u001b[K     |████████████████████████████████| 2.1 MB 44.4 MB/s \n",
            "\u001b[K     |████████████████████████████████| 634 kB 32.5 MB/s \n",
            "\u001b[K     |████████████████████████████████| 1.4 MB 34.9 MB/s \n",
            "\u001b[K     |████████████████████████████████| 52 kB 1.0 MB/s \n",
            "\u001b[K     |████████████████████████████████| 49 kB 5.1 MB/s \n",
            "\u001b[K     |████████████████████████████████| 38.2 MB 20 kB/s \n",
            "\u001b[K     |████████████████████████████████| 943 kB 31.3 MB/s \n",
            "\u001b[K     |████████████████████████████████| 3.5 MB 32.0 MB/s \n",
            "\u001b[K     |████████████████████████████████| 6.3 MB 35.4 MB/s \n",
            "\u001b[?25h  Building wheel for qiskit (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Building wheel for dlx (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Building wheel for docplex (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Building wheel for python-constraint (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Building wheel for yfinance (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "\u001b[K     |████████████████████████████████| 162 kB 5.5 MB/s \n",
            "\u001b[?25h  Building wheel for pylatexenc (setup.py) ... \u001b[?25l\u001b[?25hdone\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "CsJXnRQBP7WQ"
      },
      "source": [
        "class Board:\n",
        "    def __init__(self):\n",
        "        self.qc = QuantumCircuit(game_size, game_size)\n",
        "        self.function = ''\n",
        "        self.target = -1\n",
        "        self.tab = []\n",
        "        self.winsX = 0\n",
        "        self.winsO = 0\n",
        "        self.steps = 10 #maximum number of moves \n",
        "        print(\"Moves remaining: \" + str(self.steps))   \n",
        "\n",
        "        for idx in range(0, game_size):\n",
        "            self.tab.append({'default':str(idx), 'player':' '})\n",
        "            self.qc.reset(idx)\n",
        "            self.qc.h(idx)\n",
        "        self.qc.barrier()\n",
        "\n",
        "    def make_move(self, cell):\n",
        "        if self.function == 'Not':\n",
        "            self.qc.x(cell)\n",
        "            self.tab[int(cell)]['player'] += 'N - '  \n",
        "        elif self.function == 'O':\n",
        "            self.qc.ry(1*np.pi/2, cell)\n",
        "            self.tab[int(cell)]['player'] += \"O - \"\n",
        "        elif self.function == 'X':\n",
        "            self.qc.ry(1*-np.pi/2, cell)\n",
        "            self.tab[int(cell)]['player'] += \"X - \" \n",
        "        elif self.function == 'SWAP' and self.target != cell:\n",
        "            if self.target == cell:\n",
        "                self.target = -1\n",
        "            else:\n",
        "                self.qc.swap(cell, self.target)\n",
        "                self.tab[int(cell)]['player'] += \"S - \" \n",
        "                self.tab[int(self.target)]['player'] += \"S - \"\n",
        "        self.steps -= 1\n",
        "        print(\"Moves remaining: \" + str(self.steps))\n",
        "                          \n",
        "    def results(self):\n",
        "        display(self.qc.draw('mpl'))\n",
        "        self.qc = QuantumCircuit(game_size, game_size)\n",
        "\n",
        "    def display(self):\n",
        "        display(self.qc.draw('mpl'))\n",
        "        \n",
        "    def measure(self):\n",
        "        self.qc.barrier()\n",
        "        for i in range(0,game_size):\n",
        "            self.qc.measure(i, i)\n",
        "        \n",
        "        job = qiskit.execute(self.qc, backend, shots=1, memory=True)\n",
        "        output = job.result().get_memory()[0]\n",
        "        \n",
        "        for i in range(0,game_size):\n",
        "            if output[game_size-1-i] == '0':\n",
        "                self.tab[i]['player'] = 'X'\n",
        "            else:\n",
        "                self.tab[i]['player'] = 'O'\n",
        "        self.winsX = self.countWinners('X')\n",
        "        self.winsO = self.countWinners('O')\n",
        "\n",
        "    def countWinners(self, player):\n",
        "        if game_size == 9:\n",
        "          winners = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))\n",
        "        else:\n",
        "          winners = ((0,1),(2,3),(0,2),(1,3),(0,3),(1,2))\n",
        "        wins = 0\n",
        "        for i in range(len(winners)):\n",
        "            won = True\n",
        "            for j in range(len(winners[0])):\n",
        "                if not self.tab[winners[i][j]]['player'] == player:\n",
        "                    won = False\n",
        "            if won:\n",
        "                wins = wins + 1\n",
        "        return wins\n",
        "    \n",
        "    def new(self):\n",
        "        self.tab.clear()\n",
        "        for idx in range(0,game_size):\n",
        "           self.tab.append({'default':str(idx), 'player':''})\n",
        "           self.qc.reset(idx)\n",
        "           self.qc.h(idx)\n",
        "        self.qc.barrier()\n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "SGX8WF3wQC8V"
      },
      "source": [
        "class Game:\n",
        "    def __init__(self):\n",
        "        self.selecting = False\n",
        "        self.board = Board()\n",
        "        self.boardbutton_list = []\n",
        "        for i in range(0,game_size):\n",
        "            button = Button(description=str(i))\n",
        "            button.on_click(self.handle_game)\n",
        "            self.boardbutton_list.append(button)\n",
        "        self.funcbutton_list = []\n",
        "        self.newButton('Measure')\n",
        "        self.newButton('Not')\n",
        "        self.newButton('O')\n",
        "        self.newButton('X')\n",
        "        self.newButton('SWAP')\n",
        "        self.printmenu()\n",
        "        self.printBoard()\n",
        "\n",
        "    def newButton(self, name):\n",
        "        function = Button(description=name, layout=Layout(width='86px', height='30px'))\n",
        "        function.on_click(self.handle_game)\n",
        "        self.funcbutton_list.append(function)\n",
        "\n",
        "    def handle_game(self, b):\n",
        "        try:\n",
        "            if b.description == 'Measure':\n",
        "                clear_output()\n",
        "                self.replay()\n",
        "                self.board.measure()\n",
        "                self.scoreboard()\n",
        "                self.printBoard() \n",
        "                self.board.results()\n",
        "                \n",
        "            if b.description == 'Replay':\n",
        "                clear_output()\n",
        "                self.board.new()\n",
        "                self.printmenu()\n",
        "                self.printBoard()\n",
        "                            \n",
        "            if int(b.description) >= 0:\n",
        "                if self.selecting:\n",
        "                    self.board.target = int(b.description)\n",
        "                else:\n",
        "                    clear_output()\n",
        "                    self.printmenu()\n",
        "                    self.board.make_move(int(b.description))\n",
        "                    self.printBoard()\n",
        "                    self.board.display()\n",
        "            self.selecting = False\n",
        "        except ValueError:\n",
        "            self.board.function = b.description\n",
        "            self.selecting = False\n",
        "            if self.board.function == 'SWAP':\n",
        "                self.selecting = True\n",
        "        if self.board.steps == 0:\n",
        "            clear_output()\n",
        "            self.replay()\n",
        "            self.board.measure()\n",
        "            self.scoreboard()\n",
        "            self.printBoard() \n",
        "            self.board.results()\n",
        "            self.board.steps = 3 #reset maximum numbers of moves\n",
        "\n",
        "    def printmenu(self):\n",
        "        grid = widgets.Grid(1, 5)\n",
        "        for (row, col) in grid:\n",
        "            display(self.funcbutton_list[col])\n",
        "\n",
        "    def scoreboard(self):\n",
        "        print(\"X wins: \" + str(self.board.winsX) + \"    O wins: \" + str(self.board.winsO))\n",
        "\n",
        "    def replay(self):\n",
        "        rep = Button(description=\"Replay\")\n",
        "        rep.on_click(self.handle_game)\n",
        "        display(rep)\n",
        "\n",
        "    def printBoard(self):\n",
        "        grid = widgets.Grid(1, int(np.sqrt(game_size)), header_row=True, header_column=True)\n",
        "        for row in range(int(np.sqrt(game_size))):\n",
        "              for (useless, col) in grid:\n",
        "                  print(\"\\n\"+self.board.tab[col + row * int(np.sqrt(game_size))]['player']+\"\\n\")\n",
        "                  display(self.boardbutton_list[col + row * int(np.sqrt(game_size))])"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "sf42GkLD0cLf"
      },
      "source": [
        "backend = Aer.get_backend('aer_simulator')\n",
        "\n",
        "game_size = 9"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 809,
          "referenced_widgets": [
            "14e04589d4754c078287878fcabaa476",
            "104ba15919954ad1a32a6bcfab251ca2",
            "2deff77114ad4729b29fe60abe7cc731",
            "dc721c091aad489582e7d2315185a908",
            "599c7e30166d457ba99579c8ce841959",
            "77d5615fe95549dc9094816b826494d0",
            "d8c49f3989c94b028603f948768b219f",
            "b52160942f20420f8e9be0471b639b0a",
            "b29d7bbeb4ec4cbe8b08c7d42af66b1a",
            "299eb30a65fd4eb0ac4c339503a2eba5",
            "03332e3e638d4f8ab57b8971e4c6813b",
            "cd2219bdadec401582211c24f4bae09f",
            "459a59fe7aec4bd398065c10f0163cdb",
            "18c3d0b9515f49c6b4717aa38f025c4e",
            "52882fa4ee11469f982cc0a56b525d0f",
            "2be9e144ab5045abbbeb875b0f886fcb",
            "e924fe6b79fd4650b8cd089c157d113f",
            "651fa03154bf48368bba9d8725d26927",
            "90c0deae0349447d9c2d85a1e516efe6",
            "fcb38b2d8acb43288390d9794cb2e8f6",
            "d42a99b06ebd474a9ec829851599b240",
            "bb57b7c0d6554231a28c9ee5febb1b87",
            "bf7d9dddce4343baa0401a4afebe8c2c",
            "a87b6f5972d84cc0ad039cb8cef8b94a",
            "81fcb49ab44d41e88b2e179c601f0d59",
            "fb8ab179a8d043e9bae92f869f1a9f20",
            "05d87db07b5c4999af986b4d0486ad53",
            "f2b8e4dbab11422993b008639c9293ba",
            "12b20ca76ac9456bb63e9aa7b9579208",
            "4f6db24019f64b76ae67efb2e3f47d99",
            "7dbecb7a95b24a8c9a74f5dd2f1d4449",
            "dba1109aaa35429498c94be67d9530ba",
            "fb32dda1c58a458eac7625c406058458",
            "72e04da17254451f8e375dec1dce2b76",
            "bb874be13d0042369b922748c9c594f2",
            "c19d20deb2c84c3eabecf3952f5d9f7e",
            "ff8b733f22bc43858aa44c005ec0e7ba",
            "8a70c0ca8aa64e8f93603a896921177a",
            "892ada0e75604400921806951ab778fd",
            "1bce1417447d4d53885e8ba8ab3934c9",
            "491f3c68d5f548beaf8014bd225bfbf0",
            "b2180747aea34645a595a23828fb2259",
            "9972c454606142b9b8caa2a8edfe8e92"
          ]
        },
        "id": "wVokzg_s0vZa",
        "outputId": "bf165567-574f-4b17-e8d4-bf24061443fa"
      },
      "source": [
        "game = Game()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "application/vnd.jupyter.widget-view+json": {
              "model_id": "9972c454606142b9b8caa2a8edfe8e92",
              "version_minor": 0,
              "version_major": 2
            },
            "text/plain": [
              "Button(description='Replay', style=ButtonStyle())"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "X wins: 0    O wins: 1\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/html": [
              "<style>\n",
              "       table#id46, #id46 > tbody > tr > th, #id46 > tbody > tr > td {\n",
              "         border: 1px solid lightgray;\n",
              "         border-collapse:collapse;\n",
              "         \n",
              "        }</style>"
            ],
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/html": [
              "<table id=id46><tr><th id=id46-0-0></th><th id=id46-0-1></th><th id=id46-0-2></th></tr></table>"
            ],
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "application/javascript": [
              "window[\"ad857b76-2c2f-11ec-8636-0242ac1c0002\"] = google.colab.output.getActiveOutputArea();\n",
              "//# sourceURL=js_3252ea0c8c"
            ],
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "application/javascript": [
              "window[\"ad85da62-2c2f-11ec-8636-0242ac1c0002\"] = document.querySelector(\"#id46-0-0\");\n",
              "//# sourceURL=js_4c12820c43"
            ],
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "application/javascript": [
              "window[\"ad86394e-2c2f-11ec-8636-0242ac1c0002\"] = google.colab.output.setActiveOutputArea(window[\"ad85da62-2c2f-11ec-8636-0242ac1c0002\"]);\n",
              "//# sourceURL=js_3a817cddeb"
            ],
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "O\n",
            "\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "application/vnd.jupyter.widget-view+json": {
              "model_id": "2be9e144ab5045abbbeb875b0f886fcb",
              "version_minor": 0,
              "version_major": 2
            },
            "text/plain": [
              "Button(description='0', style=ButtonStyle())"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "application/javascript": [
              "window[\"ad881ad4-2c2f-11ec-8636-0242ac1c0002\"] = google.colab.output.setActiveOutputArea(window[\"ad857b76-2c2f-11ec-8636-0242ac1c0002\"]);\n",
              "//# sourceURL=js_f762b7f032"
            ],
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "application/javascript": [
              "window[\"ad8a56d2-2c2f-11ec-8636-0242ac1c0002\"] = google.colab.output.getActiveOutputArea();\n",
              "//# sourceURL=js_39b44ff8e5"
            ],
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "application/javascript": [
              "window[\"ad8abbb8-2c2f-11ec-8636-0242ac1c0002\"] = document.querySelector(\"#id46-0-1\");\n",
              "//# sourceURL=js_f63d35b421"
            ],
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "application/javascript": [
              "window[\"ad8b169e-2c2f-11ec-8636-0242ac1c0002\"] = google.colab.output.setActiveOutputArea(window[\"ad8abbb8-2c2f-11ec-8636-0242ac1c0002\"]);\n",
              "//# sourceURL=js_8019c24b6e"
            ],
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "O\n",
            "\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "application/vnd.jupyter.widget-view+json": {
              "model_id": "90c0deae0349447d9c2d85a1e516efe6",
              "version_minor": 0,
              "version_major": 2
            },
            "text/plain": [
              "Button(description='1', style=ButtonStyle())"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "application/javascript": [
              "window[\"ad8d0288-2c2f-11ec-8636-0242ac1c0002\"] = google.colab.output.setActiveOutputArea(window[\"ad8a56d2-2c2f-11ec-8636-0242ac1c0002\"]);\n",
              "//# sourceURL=js_ab129335a2"
            ],
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "application/javascript": [
              "window[\"ad8f38a0-2c2f-11ec-8636-0242ac1c0002\"] = google.colab.output.getActiveOutputArea();\n",
              "//# sourceURL=js_c4d00c43d5"
            ],
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "application/javascript": [
              "window[\"ad8f9c14-2c2f-11ec-8636-0242ac1c0002\"] = document.querySelector(\"#id46-0-2\");\n",
              "//# sourceURL=js_18f022af7e"
            ],
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "application/javascript": [
              "window[\"ad8ff826-2c2f-11ec-8636-0242ac1c0002\"] = google.colab.output.setActiveOutputArea(window[\"ad8f9c14-2c2f-11ec-8636-0242ac1c0002\"]);\n",
              "//# sourceURL=js_ba042d5846"
            ],
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "X\n",
            "\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "application/vnd.jupyter.widget-view+json": {
              "model_id": "bb57b7c0d6554231a28c9ee5febb1b87",
              "version_minor": 0,
              "version_major": 2
            },
            "text/plain": [
              "Button(description='2', style=ButtonStyle())"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "application/javascript": [
              "window[\"ad92012a-2c2f-11ec-8636-0242ac1c0002\"] = google.colab.output.setActiveOutputArea(window[\"ad8f38a0-2c2f-11ec-8636-0242ac1c0002\"]);\n",
              "//# sourceURL=js_3c26b57d85"
            ],
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "application/javascript": [
              "window[\"ad94fa2e-2c2f-11ec-8636-0242ac1c0002\"] = google.colab.output.getActiveOutputArea();\n",
              "//# sourceURL=js_1afc65c06d"
            ],
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "application/javascript": [
              "window[\"ad9632f4-2c2f-11ec-8636-0242ac1c0002\"] = document.querySelector(\"#id46-0-0\");\n",
              "//# sourceURL=js_bdc0431824"
            ],
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "application/javascript": [
              "window[\"ad969758-2c2f-11ec-8636-0242ac1c0002\"] = google.colab.output.setActiveOutputArea(window[\"ad9632f4-2c2f-11ec-8636-0242ac1c0002\"]);\n",
              "//# sourceURL=js_094f72ff7f"
            ],
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "X\n",
            "\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "application/vnd.jupyter.widget-view+json": {
              "model_id": "81fcb49ab44d41e88b2e179c601f0d59",
              "version_minor": 0,
              "version_major": 2
            },
            "text/plain": [
              "Button(description='3', style=ButtonStyle())"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "application/javascript": [
              "window[\"ad98995e-2c2f-11ec-8636-0242ac1c0002\"] = google.colab.output.setActiveOutputArea(window[\"ad94fa2e-2c2f-11ec-8636-0242ac1c0002\"]);\n",
              "//# sourceURL=js_7e2f9a0e7e"
            ],
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "application/javascript": [
              "window[\"ad9aecea-2c2f-11ec-8636-0242ac1c0002\"] = google.colab.output.getActiveOutputArea();\n",
              "//# sourceURL=js_dc8f9c8df3"
            ],
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "application/javascript": [
              "window[\"ad9b4d16-2c2f-11ec-8636-0242ac1c0002\"] = document.querySelector(\"#id46-0-1\");\n",
              "//# sourceURL=js_ffc6e91786"
            ],
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "application/javascript": [
              "window[\"ad9ba64e-2c2f-11ec-8636-0242ac1c0002\"] = google.colab.output.setActiveOutputArea(window[\"ad9b4d16-2c2f-11ec-8636-0242ac1c0002\"]);\n",
              "//# sourceURL=js_7b0f74b3d4"
            ],
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "X\n",
            "\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "application/vnd.jupyter.widget-view+json": {
              "model_id": "f2b8e4dbab11422993b008639c9293ba",
              "version_minor": 0,
              "version_major": 2
            },
            "text/plain": [
              "Button(description='4', style=ButtonStyle())"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "application/javascript": [
              "window[\"ad9d8a86-2c2f-11ec-8636-0242ac1c0002\"] = google.colab.output.setActiveOutputArea(window[\"ad9aecea-2c2f-11ec-8636-0242ac1c0002\"]);\n",
              "//# sourceURL=js_2be8800643"
            ],
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "application/javascript": [
              "window[\"ad9fbe50-2c2f-11ec-8636-0242ac1c0002\"] = google.colab.output.getActiveOutputArea();\n",
              "//# sourceURL=js_ccdd3ec2b9"
            ],
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "application/javascript": [
              "window[\"ada02cc8-2c2f-11ec-8636-0242ac1c0002\"] = document.querySelector(\"#id46-0-2\");\n",
              "//# sourceURL=js_7ef5668a98"
            ],
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "application/javascript": [
              "window[\"ada08b82-2c2f-11ec-8636-0242ac1c0002\"] = google.colab.output.setActiveOutputArea(window[\"ada02cc8-2c2f-11ec-8636-0242ac1c0002\"]);\n",
              "//# sourceURL=js_b3a9a6088a"
            ],
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "O\n",
            "\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "application/vnd.jupyter.widget-view+json": {
              "model_id": "7dbecb7a95b24a8c9a74f5dd2f1d4449",
              "version_minor": 0,
              "version_major": 2
            },
            "text/plain": [
              "Button(description='5', style=ButtonStyle())"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "application/javascript": [
              "window[\"ada28f90-2c2f-11ec-8636-0242ac1c0002\"] = google.colab.output.setActiveOutputArea(window[\"ad9fbe50-2c2f-11ec-8636-0242ac1c0002\"]);\n",
              "//# sourceURL=js_f754f200d1"
            ],
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "application/javascript": [
              "window[\"ada4d390-2c2f-11ec-8636-0242ac1c0002\"] = google.colab.output.getActiveOutputArea();\n",
              "//# sourceURL=js_d33476a8f3"
            ],
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "application/javascript": [
              "window[\"ada52e9e-2c2f-11ec-8636-0242ac1c0002\"] = document.querySelector(\"#id46-0-0\");\n",
              "//# sourceURL=js_5aef663d1d"
            ],
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "application/javascript": [
              "window[\"ada58876-2c2f-11ec-8636-0242ac1c0002\"] = google.colab.output.setActiveOutputArea(window[\"ada52e9e-2c2f-11ec-8636-0242ac1c0002\"]);\n",
              "//# sourceURL=js_9a9dc42cfe"
            ],
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "O\n",
            "\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "application/vnd.jupyter.widget-view+json": {
              "model_id": "72e04da17254451f8e375dec1dce2b76",
              "version_minor": 0,
              "version_major": 2
            },
            "text/plain": [
              "Button(description='6', style=ButtonStyle())"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "application/javascript": [
              "window[\"ada7796a-2c2f-11ec-8636-0242ac1c0002\"] = google.colab.output.setActiveOutputArea(window[\"ada4d390-2c2f-11ec-8636-0242ac1c0002\"]);\n",
              "//# sourceURL=js_a04058f58e"
            ],
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "application/javascript": [
              "window[\"ada9bd7e-2c2f-11ec-8636-0242ac1c0002\"] = google.colab.output.getActiveOutputArea();\n",
              "//# sourceURL=js_6c3f4ef7a7"
            ],
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "application/javascript": [
              "window[\"adaa1cc4-2c2f-11ec-8636-0242ac1c0002\"] = document.querySelector(\"#id46-0-1\");\n",
              "//# sourceURL=js_96d7da0d4f"
            ],
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "application/javascript": [
              "window[\"adaa7520-2c2f-11ec-8636-0242ac1c0002\"] = google.colab.output.setActiveOutputArea(window[\"adaa1cc4-2c2f-11ec-8636-0242ac1c0002\"]);\n",
              "//# sourceURL=js_73587780f1"
            ],
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "O\n",
            "\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "application/vnd.jupyter.widget-view+json": {
              "model_id": "ff8b733f22bc43858aa44c005ec0e7ba",
              "version_minor": 0,
              "version_major": 2
            },
            "text/plain": [
              "Button(description='7', style=ButtonStyle())"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "application/javascript": [
              "window[\"adac79a6-2c2f-11ec-8636-0242ac1c0002\"] = google.colab.output.setActiveOutputArea(window[\"ada9bd7e-2c2f-11ec-8636-0242ac1c0002\"]);\n",
              "//# sourceURL=js_e4610baa3d"
            ],
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "application/javascript": [
              "window[\"adaf0202-2c2f-11ec-8636-0242ac1c0002\"] = google.colab.output.getActiveOutputArea();\n",
              "//# sourceURL=js_fbef71e0e6"
            ],
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "application/javascript": [
              "window[\"adaf7b06-2c2f-11ec-8636-0242ac1c0002\"] = document.querySelector(\"#id46-0-2\");\n",
              "//# sourceURL=js_0f0617f1b9"
            ],
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "application/javascript": [
              "window[\"adaffdf6-2c2f-11ec-8636-0242ac1c0002\"] = google.colab.output.setActiveOutputArea(window[\"adaf7b06-2c2f-11ec-8636-0242ac1c0002\"]);\n",
              "//# sourceURL=js_424ebdb61c"
            ],
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "O\n",
            "\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "application/vnd.jupyter.widget-view+json": {
              "model_id": "1bce1417447d4d53885e8ba8ab3934c9",
              "version_minor": 0,
              "version_major": 2
            },
            "text/plain": [
              "Button(description='8', style=ButtonStyle())"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "application/javascript": [
              "window[\"adb24e9e-2c2f-11ec-8636-0242ac1c0002\"] = google.colab.output.setActiveOutputArea(window[\"adaf0202-2c2f-11ec-8636-0242ac1c0002\"]);\n",
              "//# sourceURL=js_e621b2a9e1"
            ],
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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DNWfItWkiQrPPBEm2YIPABGhvdHGXn96XN8e3pIo+IAMSv6JEyfw9NNPw8HBAc2aNUOXLl3q7euwu3eL8dNvaSi+V1LpFywRkamE9g3Qm8M+JkINq+bNBCYyzM6mBUaG99f93LWja6UCLUWPh/bWzWFXKhV45smBsLCQ9h1V27axx1D1/TnsPXy6wsfAOQaiKRQKjBo2QDeHvWnF1JF6njv9qDzcnDGg1/0PIure/gbPMRBNpVQi6okwNP2/cWzTojlGDh0g2YMEFfy6eSDQ+/4c9gh1bzg61HyOgWhNLZog6skw3RSoNvZ2NU5fbGjS/ttlwJEjR9CnTx+kp6dj1apV+PbbbzFv3jz88ccf9bK/n4+m4/aduxjcr6fhlYmI6kilVOKZJ8NgYdEEfQK90NWj+vmqUuLv1Rn+3TuheTNLjI5QS75UAPfLpkKhwOB+PeHi5CA6klH6BfnCo307tLS1RuRgaU4tepi1VXOMiggBADw1qC/sW9bPibOmFj4gGE5t7OHs2BqD+5vHv/+tW9nqTmgdHaFGCytpHySoEDm4H+xsWqCzu4vBKxdJhZuzIwY+1gPK//uWp6mEDhKY9Zz80NBQnDp1Cr///rvuDn7GmhezoZ5SERERERHVjxVzpxi1ntkeyb99+zYOHDiAcePG1brgExERERHJmXS+U6ilmzdvorS0tM43eTH2UxBQPhc/5v2tcGvniEljIuq0PyIiIiKihmK2Jb9Vq1ZQKpW6mwjUVl2m62Scv8RpPkREREQkjOyn61hZWSEkJARbt26tt1tbExERERGZI7M+8fbIkSMICQmBu7s75syZA3d3d2RnZ+PAgQMmuztbxU0lpj03Am7tpHNbdiIiIiKi6pjtdB0A6NmzJ3755Re8+eabmDFjBu7cuQM3NzeMHTvWJNu/e7cYBw4dh6eHGws+EREREZkNsz6SX9+u5l7HZzuSMPbJgSz5RERERGQ2WPINKC0tlfwd+YiIiIiIHsSST0REREQkMzxETUREREQkMyz5REREREQyw5JPRERERCQzLPlERERERDLDkk9EREREJDMs+UREREREMsOST0REREQkMyz5REREREQyw5JPRERERCQzLPlERERERDLDkk9EREREJDMs+UREREREMsOST0REREQkMyz5REREREQyw5JPRERERCQzLPlERERERDLDkk9EREREJDMs+UREREREMsOST0REREQkMyz5REREREQyw5JPRERERCQzLPlERERERDLDkk9EREREJDMs+UREREREMsOST0REREQkMyz5REREREQyw5JPRERERCQz/x/1yyxX5GnykgAAAABJRU5ErkJggg==\n",
            "text/plain": [
              "<Figure size 989.597x626.08 with 1 Axes>"
            ]
          },
          "metadata": {}
        }
      ]
    }
  ]
}