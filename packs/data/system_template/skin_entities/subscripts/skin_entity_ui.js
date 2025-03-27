//@ts-check

import {
	world,
	system,
	Entity,
	Player,
	EntityMarkVariantComponent,
	Camera,
	EntitySkinIdComponent,
} from "@minecraft/server";
import {
	ActionFormData,
	ModalFormData,
	MessageFormData,
} from "@minecraft/server-ui";

// Executes whenever the /scriptevent command is being executed ingame.
system.afterEvents.scriptEventReceive.subscribe((event) => {
	if (event.sourceEntity == undefined) {
		throw new Error(
			`Failed to get source entity from the called script event. Are you calling this from the console?`,
		);
	}
	if (event.id == "shapescape:open_skin_entity_ui") {
		openSceneMain(event.sourceEntity, getPlayersByName(event.message));
	}
});

/**
 *
 * @param {string} player_name
 * @returns Player
 */
function getPlayersByName(player_name) {
	let players = world.getPlayers({ name: player_name });
	if (players.length == 1) {
		return players[0];
	}
	throw new Error(`Could not get a player by that name: ${player_name}.`);
}

// Custom implementation of pythons .title() method that capitalizes the first character of each word in a string
function titleCase(str) {
	return str
		.toLowerCase()
		.split(" ")
		.map(function (word) {
			return word.charAt(0).toUpperCase() + word.slice(1);
		})
		.join(" ");
}

function getCurrentSkin(skinEntity) {
	let variant = /** @type {EntitySkinIdComponent | undefined} */ (
		/** @type {any} */ (skinEntity.getComponent("minecraft:skin_id"))
	);
	if (variant?.isValid) {
		return variant.value;
	} else {
		return 0;
	}
}

function getCurrentPose(skinEntity) {
	let variant = /** @type {EntityMarkVariantComponent | undefined} */ (
		/** @type {any} */ (skinEntity.getComponent("minecraft:mark_variant"))
	);
	if (variant?.isValid) {
		return variant.value;
	} else {
		return 0;
	}
}

/**
 *
 * @param {Entity} skinEntity
 * @param {Player} player_source
 */
function openSceneMain(skinEntity, player_source) {
	const homeButtonHandlers = [];
	let form = new ActionFormData();
	form.title("Skin Entity UI");
	form.button("Change Skin", "textures/ui/skin");
	homeButtonHandlers.push(() => {
		openSkinChangeScene(skinEntity, player_source);
	});
	form.button("Change Pose", "textures/ui/pose");
	homeButtonHandlers.push(() => {
		openPoseChangeScene(skinEntity, player_source);
	});
	form.button("Rotate To Me", "textures/items/armor_stand");
	homeButtonHandlers.push(() => {
		skinEntity.runCommand(`/teleport @s ~ ~ ~ facing @p`);
	});
	// form.button("Physics", "textures/items/wind_charge");
	// homeButtonHandlers.push(() => {
	// 	skinEntity.remove();
	// });
	form.button("Reset", "textures/ui/reset");
	homeButtonHandlers.push(() => {
		skinEntity.runCommand("/event entity @s shapescape:default");
		skinEntity.runCommand("/event entity @s shapescape:pose_none");
	});
	form.button("Despawn", "textures/ui/delete");
	homeButtonHandlers.push(() => {
		skinEntity.remove();
	});

	form.show(player_source).then((r) => {
		// Check if the form was canceled
		if (r.canceled) {
			return;
		}
		// Process the player's selection and set the corresponding mode
		let response = r.selection;
		if (response == undefined) {
			return;
		}

		homeButtonHandlers[response]();
	});
}

function openSkinChangeScene(skinEntity, player_source) {
	let skins = ["placeholder"];
	// This gets replaced with with a list of all skins by a custom system template plugin
	const dynamicly_loaded_skins = [/*@skins_list*/]; // prettier-ignore

	skins = skins.concat(dynamicly_loaded_skins);

	let skinsDisplayed = [];

	// For loop that goes over all the strings in skins, ttileCases it, replaces "_" with " ", puts the a or s at the end in () and adds it to skinsDisplayed
	for (let i = 0; i < skins.length; i++) {
		let skin = skins[i];
		skinsDisplayed.push(titleCase(skin.replace(/_/g, " ")));
	}

	const homeButtonHandlers = [];
	let form = new ModalFormData();
	form.title("Skin Entity UI");
	form.dropdown("Select Skin", skinsDisplayed, getCurrentSkin(skinEntity));

	homeButtonHandlers.push((value) => {
		skinEntity.runCommand(`/event entity @s shapescape:skin.${skins[value]}`);
	});

	form.show(player_source).then((r) => {
		// Check if the form was canceled
		if (r.canceled) {
			return;
		}
		// Process the player's selection and set the corresponding mode
		if (r.formValues != undefined) {
			homeButtonHandlers[0](r.formValues[0]);
		}
	});
}

function openPoseChangeScene(skinEntity, player_source) {
	let poses = ["none"];
	// This gets replaced with with a list of all skins by a custom system template plugin
	const dynamicly_loaded_poses = [/*@animation_names*/]; // prettier-ignore

	poses = poses.concat(dynamicly_loaded_poses);

	let posesDisplayed = [];

	// For loop that goes over all the strings in skins, ttileCases it, replaces "_" with " ", puts the a or s at the end in () and adds it to skinsDisplayed
	for (let i = 0; i < poses.length; i++) {
		let skin = poses[i];
		posesDisplayed.push(titleCase(skin.replace(/_/g, " ")));
	}

	const homeButtonHandlers = [];
	let form = new ModalFormData();
	form.title("Skin Entity UI");
	form.dropdown("Select Pose", posesDisplayed, getCurrentPose(skinEntity));

	homeButtonHandlers.push((value) => {
		skinEntity.runCommand(`/event entity @s shapescape:pose.${poses[value]}`);
	});

	form.show(player_source).then((r) => {
		// Check if the form was canceled
		if (r.canceled) {
			return;
		}
		// Process the player's selection and set the corresponding mode
		if (r.formValues != undefined) {
			homeButtonHandlers[0](r.formValues[0]);
		}
	});
}
