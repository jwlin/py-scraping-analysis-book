/*
 * [y] hybris Platform
 *
 * Copyright (c) 2017 SAP SE or an SAP affiliate company. All rights reserved.
 *
 * This software is the confidential and proprietary information of SAP
 * ("Confidential Information"). You shall not disclose such Confidential
 * Information and shall use it only in accordance with the terms of the
 * license agreement you entered into with SAP.
 */
window.smartedit = window.smartedit || {};

window.smartedit.reprocessPage = function(){

	// reinitializing the list of images processed through the Imager object
	ACC.global.initImager();

	// replacing images according to screen size, when required
	ACC.global.reprocessImages();

	// replaying the my account nav only if it has been swapped by new component
	if($(".navigation--top .myAccountLinksHeader").length===0) {
		$('.js-myAccount-root').empty();
		$(".js-secondaryNavAccount > ul").empty();
		ACC.navigation.myAccountNavigation();
	}

	// Make sure the carousel component is reloaded properly after re-rendering.
	ACC.carousel.bindCarousel();

}
