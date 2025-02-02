import { app } from "../../../../scripts/app.js";



let origProps = {};
export const findWidgetByName = (node, name) => node.widgets.find((w) => w.name === name);

export function updateNodeHeight(node) {node.setSize([node.size[0], node.computeSize()[1]]);}

export function toggleWidget(node, widget, show = false,) {
  if(!widget) return;

	if (!origProps[widget.name]) {
		origProps[widget.name] = { origType: widget.type, origComputeSize: widget.computeSize };
	}
	const origSize = node.size;

	widget.type = show ? origProps[widget.name].origType : "easyHidden" ;
	widget.computeSize = show ? origProps[widget.name].origComputeSize : () => [0, -4];

	widget.linkedWidgets?.forEach(w => toggleWidget(node, w, ":" + widget.name, show));

	const height = show ? Math.max(node.computeSize()[1], origSize[1]) : node.size[1];
	node.setSize([node.size[0], height]);
}









function widgetLogic(node, widget) {

	if (widget.name === 'num_loras') {
		let number_to_show = widget.value
		for (let i = 0; i < number_to_show; i++) {
			toggleWidget(node, findWidgetByName(node, 'lora_'+i+'_name'), true);
		}
		for (let i = number_to_show; i < 21; i++) {
			toggleWidget(node, findWidgetByName(node, 'lora_'+i+'_name'));
		}
		updateNodeHeight(node);
	} else if (widget.name === "num_ckpts") {
		let number_to_show = widget.value
		for (let i = 0; i < number_to_show; i++) {
			toggleWidget(node, findWidgetByName(node, 'ckpt_'+i+'_name'), true);
		}
		for (let i = number_to_show; i < 21; i++) {
			toggleWidget(node, findWidgetByName(node, 'ckpt_'+i+'_name'));
		}
		updateNodeHeight(node);
	}

}



app.registerExtension({
	name: "comfy.selector.dynamicWidgets",

	nodeCreated(node) {
		switch (node.comfyClass){

			case "lora selector":
			case "ckpt selector":
				getSetters(node);
				break;
		}

	},

});


const getSetWidgets = ['num_loras', 'num_ckpts']

function getSetters(node) {
	if (node.widgets)
		for (const w of node.widgets) {
			if (getSetWidgets.includes(w.name)) {
				widgetLogic(node, w);
				let widgetValue = w.value;

				// Define getters and setters for widget values
				Object.defineProperty(w, 'value', {
					get() {
						return widgetValue;
					},
					set(newVal) {
						if (newVal !== widgetValue) {
							widgetValue = newVal;
							widgetLogic(node, w);
						}
					}
				});
			}
		}
}